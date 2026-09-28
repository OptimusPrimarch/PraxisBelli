"""
Praxis Belli points calculator.

Implements the formula in design-bible.md section 11.

Rebuilt from a bare slate 2026-09-28 for the d6 conversion -- every constant
and function below is new, not patched from the old d10-era version. See
design-bible.md SS11 for the full reasoning behind each piece; this file
mirrors that section closely enough that the two should be read together.

Usage:
    python points.py                 # cost the built-in reference roster
    python points.py roster.json     # cost a roster file
"""

import json
import sys

# ---------------------------------------------------------------- constants

# Currency scale. These two move together: multiplying both by the same factor
# rescales every cost in the game proportionally without altering any relative
# balance -- it is a pure unit conversion. Calibrated at the 80/20 model/weapon
# split so that the anchor unit -- a 10-model Rifle Squad, CCW only, no
# bayonet by default -- lands on exactly 100 points (80 chassis + 20 weapons).
# 70/30 remains fully viable (BASE_MODEL 5.65 / BASE_WEAPON 19.29, Rifle 3.00)
# -- nothing about either formula favours one split technically; 80/20 was
# kept because it's what was already decided.
BASE_MODEL = 6.45          # a baseline grunt (Eva 5, Arm 4, Spd 5, Met 4, W1)
BASE_WEAPON = 12.857        # scales weapon Value into points
REF_AP = 1                  # reference AP used to normalise the Armor table
                            # (AP scale: 0 = assault rifle, 1 = magnum cartridge
                            #  / 20mm autocannon, 2 = WWII 37mm/57mm, 3 = 76mm/
                            #  88mm, 4 = modern 120mm sabot/railgun)

# Reference targets for weapon costing. Soft = the anchor's own Infantry stat
# line (no longer an arbitrary invented pairing -- Evasion 5 is literally what
# Infantry means under the archetype template, design-bible.md SS3). Hard =
# Heavy Vehicle archetype, already deep enough to engage the real Armor
# cascade mechanic.
SOFT_EVASION, SOFT_ARMOR = 5, 4
HARD_EVASION, HARD_ARMOR = 3, 8

# Trait modifiers. Every trait is multiplicative, on principle: a trait's
# value scales with how much the weapon already does, so its cost should too.
# Three grades instead of the old two, replacing the old bonus/restriction
# split -- graded by how much a trait shifts the math of the attack, OR
# whether it changes a unit's state as part of resolving it (a state change,
# like a suppression marker, counts the same as a probability shift even
# when it touches none of the attack's own numbers).
TIER_MINUSCULE_BONUS = 1.05
TIER_MINOR_BONUS = 1.15
TIER_MAJOR_BONUS = 1.35
TIER_MINUSCULE_RESTRICTION = 0.95
TIER_MINOR_RESTRICTION = 0.85
TIER_MAJOR_RESTRICTION = 0.65

# First-pass classification (design-bible.md SS11 Step 3) -- not exhaustive,
# refine as more traits get built. Anything not listed here costs nothing
# extra yet, same "shape locked, tier not assigned" status the old file used
# for Optics/Crushing/Shotgun/Meltdown.
MINUSCULE_BONUS_TRAITS = {"accurate", "pistol", "armored front"}
MINOR_BONUS_TRAITS = {"suppressing", "optics", "onslaught"}
MAJOR_BONUS_TRAITS = {"guided", "linked-weapon", "indirect", "overcharge"}
MINOR_RESTRICTIONS = {"traversing", "coaxial"}
MAJOR_RESTRICTIONS = {"heavy", "frontal arc", "rear arc", "side arc", "consumable (1)"}

MULT_TRAITS = {
    **{t: TIER_MINUSCULE_BONUS for t in MINUSCULE_BONUS_TRAITS},
    **{t: TIER_MINOR_BONUS for t in MINOR_BONUS_TRAITS},
    **{t: TIER_MAJOR_BONUS for t in MAJOR_BONUS_TRAITS},
    **{t: TIER_MINUSCULE_RESTRICTION for t in set()},  # none classified yet
    **{t: TIER_MINOR_RESTRICTION for t in MINOR_RESTRICTIONS},
    **{t: TIER_MAJOR_RESTRICTION for t in MAJOR_RESTRICTIONS},
}

# Anti-[Keyword] is priced separately, additively -- NOT a multiplier anymore
# (that was the old ×1.20 system, retired 2026-09-28). See anti_keyword_
# surcharge() below. Generalises to any keyword now, not a fixed 12/13-label
# list, but the surcharge still needs to know whether a given keyword reads
# as a soft-type (Infantry-like) or hard-type (Vehicle-like) target to price
# against the right reference. Anything unrecognised defaults to soft, since
# that's the more common case on this roster so far.
ANTI_X_WEIGHT = 0.5   # borrowed from the base formula's own soft/hard split,
                       # not a separately invented discount
SOFT_KEYWORDS = {"infantry", "cavalry", "command", "line", "shock",
                  "support", "recon", "caster"}
HARD_KEYWORDS = {"vehicle", "armor", "monster", "aerial", "towable"}

# Named/special unit abilities are FLAT costs, not multipliers -- an ability
# is a capability, not a modifier on a base the unit already has. Now three
# tiers matching the weapon-trait naming, anchored off BASE_MODEL rather than
# derived from probability (no clean probability basis exists for "how much
# is an aura worth", same status as Speed's own coefficient below).
ABILITY_MINUSCULE = 2
ABILITY_MINOR = 6
ABILITY_MAJOR = 15
ABILITY_COST = {"minuscule": ABILITY_MINUSCULE, "minor": ABILITY_MINOR, "major": ABILITY_MAJOR}

# Transport capacity, deliberately NOT forced through the 80/20 split --
# capacity is neither chassis durability nor a weapon, it's a third kind of
# value (pure delivery convenience). X is measured in seats now, not models
# (see the Size stat, design-bible.md's Reference -- Unit Profile / SS10).
TRANSPORT_RATE = 0.5


# ---------------------------------------------------------------- primitives

def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def p_hit(evasion):
    """
    Chance an Attack Roll succeeds against this Evasion, on a d6.

    Floor/ceiling baked in directly (1/6 to 5/6) rather than the old d10-era
    (0.1, 0.9) clamp -- a natural 1 always fails, a natural 6 always succeeds,
    regardless of target number. Evasion above 6 cascades exactly like Armor
    above 6 (see p_damage) -- reachable only through modifier stacking, never
    a base value, but the game doesn't forbid it.
    """
    if evasion <= 6:
        return clamp((7 - evasion) / 6, 1 / 6, 5 / 6)
    return (1 / 6) * p_hit(evasion - 6)


def p_damage(armor, ap=0):
    """
    Chance a hit converts to a wound against this Armor, after AP, on a d6.

    AP floor (design-bible.md SS3, "Armor's floor"): AP can only reduce
    effective Armor to 2, never lower -- max(armor - ap, 2). This IS the AP
    overkill cap; there's no separate Armor 1/0/-1 to land on identically; the
    formula simply never lets effective Armor reach them.

    Cascade (SS3, "Armor above 6", mechanic unchanged from the original d10
    version, just re-anchored): once effective Armor exceeds 6, an unmodified
    6 buys a second roll against (effective - 6), recursing as needed. This is
    the REAL combat probability -- see armor_factor() below for why it isn't
    mirrored 1:1 into cost.
    """
    eff = max(armor - ap, 2)
    if eff <= 6:
        return clamp((7 - eff) / 6, 1 / 6, 5 / 6)
    return (1 / 6) * p_damage(eff - 6, 0)


def p_morale_pass(mettle, markers=0):
    """
    Chance a Morale test passes: 2d6 + Mettle >= 10 + markers.

    Floor/ceiling: a natural 2 always fails, a natural 12 always passes,
    same universal principle as the d6 engine, just on the wider pool this
    specific check uses (design-bible.md SS5).
    """
    target = 10 + markers - mettle
    dist = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    if target <= 2:
        return 35 / 36
    if target >= 12:
        return 1 / 36
    return sum(c for s, c in dist.items() if s >= target) / 36


# ---------------------------------------------------------------- model cost

def evasion_factor(evasion):
    """
    sqrt(1/P_hit), normalised so Evasion 5 == 1.00 (the anchor's own stat --
    Evasion 5 is now literally the Infantry archetype baseline, not a
    separate hand-picked reference point the way Evasion 6 used to be).

    The square root is load-bearing, not decorative: a raw 1/P blows up hard
    once Armor's cascade mechanic is in play (a Bastion-grade chassis priced
    over 2000 points on the chassis alone before this fix). Evasion never
    actually needed the dampening on its own -- it's capped at 6 as a base
    value and never reaches cascade territory in practice -- but it uses the
    same transform as Armor for consistency, since the underlying
    "durability costs superlinearly" principle is the same for both.
    """
    ref = p_hit(5)
    return (ref / p_hit(evasion)) ** 0.5


def armor_factor(armor):
    """sqrt(1/P_damage) vs REF_AP, normalised so Armor 4 == 1.00."""
    ref = p_damage(4, REF_AP)
    return (ref / p_damage(armor, REF_AP)) ** 0.5


def mettle_factor(mettle):
    """
    sqrt(1/P_fail), normalised so Mettle 4 == 1.00.

    Priced off P(FAIL), not P(pass) -- a natural mistake to make and worth
    getting right: Mettle's good outcome is passing, the opposite direction
    from Evasion/Armor where the ATTACKER's bad outcome (missing, failing to
    wound) is what the target wants. Pricing off 1/P(pass) would make higher
    Mettle cheaper, which is backwards.
    """
    ref_fail = 1 - p_morale_pass(4)
    this_fail = 1 - p_morale_pass(mettle)
    return (ref_fail / this_fail) ** 0.5


def speed_factor(speed):
    """
    Zero/one-anchored ladder, not derived from probability -- movement
    doesn't map onto a hit or wound chance, so this stays hand-tuned, same
    status as Mettle's own marker-check rate used to be before it got a real
    derivation.

    Speed 0 is a discrete "Immobile" tax (0.70), not a continuation of the
    curve below it -- true immobility is a real, separate liability from
    merely being slow. Speed 1 is the free/neutral reference point (1.00).
    Every point above that adds a flat 6%.
    """
    if speed <= 0:
        return 0.70
    return 1 + 0.06 * (speed - 1)


def model_cost(speed, mettle, evasion, armor, wounds):
    e = evasion_factor(evasion)
    a = armor_factor(armor)
    s = speed_factor(speed)
    m = mettle_factor(mettle)
    return BASE_MODEL * wounds * e * a * s * m


# --------------------------------------------------------------- weapon cost

def is_melee(rng):
    return isinstance(rng, str) and rng.strip().lower() in ("m", "melee")


def range_multiplier(rng):
    """
    rng is inches, or the string 'M'/'melee' for melee weapons.

    Carried forward unexamined from the old formula -- flagged, not fixed.
    This doesn't connect to the Close/Effective/Long band mechanic
    (design-bible.md SS3) at all; it's a separate "longer reach is worth
    more" assumption that's never been re-derived.
    """
    if is_melee(rng):
        return 0.85
    return 0.6 + float(rng) / 30


def anti_keyword_surcharge(attacks, damage, rng, keyword, melee=False):
    """
    Additive surcharge for one Anti-[Keyword] tag, added ON TOP of the
    weapon's normal cost -- not multiplied in, unlike the retired ×1.20
    system. See design-bible.md SS11 for the full derivation; the short
    version:

    The bonus (natural 6 on the Attack Roll -> immediate free hit for the
    weapon's own Damage, bypassing Armor and AP entirely) needs no P_hit/
    P_damage lookup at all, since a natural 6 always hits regardless of the
    target's real Evasion, and the bonus skips the Wound Roll. It's matched
    to the SPECIFIC keyword's own reference target (soft-only or hard-only,
    never blended -- the bonus only ever triggers against one or the other)
    and respects the same overkill cap as the base formula. The x0.5 weight
    is borrowed directly from the base formula's own soft/hard split, not a
    new invented discount -- Anti-Infantry only pays off on the half of
    encounters the base formula already assumes are soft-target ones.

    Verified against a fair benchmark (the cost of doubling the weapon's own
    Attacks -- a true dice-for-dice comparison, since the bonus can trigger
    off every one of a weapon's existing attack dice): every case checked
    lands at 0.28x-0.67x of that benchmark.
    """
    kw = keyword.lower().strip()
    is_hard = kw in HARD_KEYWORDS
    dmg_term = damage if is_hard else min(damage, 1)
    value = attacks * (1 / 6) * dmg_term * ANTI_X_WEIGHT
    return BASE_WEAPON * range_multiplier(rng if not melee else "melee") * value


def weapon_cost(rng, attacks, ap, damage, traits=()):
    traits = [t.strip().lower() for t in traits]

    # CCW (replacing Fists). Every model carries one, and it's flat 0 points
    # by decision, not derivation -- "it exists solely to give each unit a
    # melee option," never run through this formula at all. Real melee
    # weapons now price at their full value below, not a margin over CCW --
    # margin over zero is just the weapon's own value, so the old
    # unarmed_value() subtraction is retired along with this.
    if "unarmed" in traits:
        return 0.0

    p_soft = p_damage(SOFT_ARMOR, ap)
    p_hard = p_damage(HARD_ARMOR, ap)

    # Overkill cap corrected to min(damage, 1) -- the anchor's real Wounds is
    # 1, so anything above that is exactly as wasted against it as Damage 8
    # would be. The old cap of 2 was quietly overvaluing every Damage-2+
    # weapon's soft-target performance.
    soft = attacks * p_hit(SOFT_EVASION) * p_soft * min(damage, 1)
    hard = attacks * p_hit(HARD_EVASION) * p_hard * damage
    value = (soft + hard) / 2

    cost = BASE_WEAPON * value * range_multiplier(rng)

    # The old "penetration x volume premium" term is dropped entirely -- it
    # was compensating for a flaw the d10 formula had that doesn't exist
    # here. Value already multiplies Attacks x P_damage(AP) INSIDE itself,
    # against both reference targets -- that's already the real
    # multiplicative relationship the premium term was trying to bolt on
    # separately a second time.

    for t in traits:
        if t in MULT_TRAITS:
            cost *= MULT_TRAITS[t]

    # Anti-[Keyword] surcharges are additive, applied after the multiplicative
    # trait tiers above, one per matching trait (e.g. "anti-infantry").
    for t in traits:
        if t.startswith("anti-"):
            keyword = t[len("anti-"):]
            cost += anti_keyword_surcharge(attacks, damage, rng, keyword,
                                            melee=is_melee(rng))

    return cost


def transport_cost(seats):
    """X is measured in seats now (Size stat), not models."""
    return seats * TRANSPORT_RATE


# ------------------------------------------------------------------ costing

def cost_unit(unit):
    """Cost one unit dict. Returns (total, breakdown_lines)."""
    lines = []
    p = unit["profile"]
    size = unit.get("size", 1)
    wounds = p.get("wounds", p.get("toughness"))  # accepts either key during
                                                    # the roster's own stale
                                                    # transition period

    per_model = model_cost(p["speed"], p["mettle"], p["evasion"],
                           p["armor"], wounds)
    chassis = per_model * size
    lines.append(f"    chassis  {size} x {per_model:6.2f} = {chassis:7.2f}")

    total = chassis

    for w in unit.get("weapons", []):
        n = w.get("count", size)
        each = weapon_cost(w["range"], w["attacks"], w["ap"],
                           w["damage"], w.get("traits", []))
        sub = each * n
        traits = ", ".join(w.get("traits", [])) or "-"
        lines.append(f"    {w['name']:<22} {n} x {each:6.2f} = {sub:7.2f}   [{traits}]")
        total += sub

    if "transport" in unit:
        t = transport_cost(unit["transport"])
        lines.append(f"    Transport({unit['transport']} seats){'':<4} {t:20.2f}")
        total += t

    # Unit size scaling: flat Model Cost x N, no discount. The old sublinear
    # Size Factor is retired outright (confirmed 2026-09-28, "no discounts,
    # we'll address it with single-model damage scaling separately") --
    # single-model toughness now goes through the Damage Track mechanic
    # (design-bible.md SS5) instead of an ever-bigger Wounds stat multiplying
    # into an ever-bigger cost. Nothing to do here; chassis above already IS
    # per_model x size with no further curve applied.

    # Faction signature trait. Hand-priced multiplier on the unit total --
    # these are the least-defensible numbers in the system, still using
    # pre-rebuild guesses (Oathbound, Bound Spirit, Martyrs/all, Wrathbound)
    # until they're re-derived against the new currency scale.
    ft = unit.get("faction_trait")
    if ft and size >= ft.get("min_size", 0):
        mult = ft.get("multiplier", 1.0)
        scaled = total * mult
        lines.append(
            f"    {ft['name']:<22} x{mult:.2f}{'':<12} {scaled - total:+8.2f}   [faction]"
        )
        total = scaled

    # Per-unit trait multipliers (Conscript, Mindless, and anything else that
    # modifies what a unit is worth rather than what it can do).
    for mod in unit.get("modifiers", []):
        mult = mod.get("multiplier", 1.0)
        scaled = total * mult
        lines.append(
            f"    {mod['name']:<22} x{mult:.2f}{'':<12} {scaled - total:+8.2f}   [trait]"
        )
        total = scaled

    # Special/named abilities are flat and sit outside unit-count scaling --
    # they usually attach to one model (a leader's aura), not the whole
    # squad.
    for extra in unit.get("extras", []):
        tier = extra.get("tier")
        cost = ABILITY_COST[tier] if tier else extra["cost"]
        label = tier or "hand-priced"
        lines.append(f"    {extra['name']:<22} {cost:26.2f}   [{label}]")
        total += cost

    return total, lines


def cost_roster(roster):
    out = []
    grand = 0
    name = roster.get("name", "Roster")
    out.append(f"=== {name} ===\n")
    for unit in roster["units"]:
        total, lines = cost_unit(unit)
        grand += total
        tags = "/".join(filter(None, [unit.get("role", unit.get("category")),
                                       unit.get("keyword", unit.get("type"))]))
        out.append(f"{unit['name']}  [{tags}]  -> {round(total)} pts")
        out.extend(lines)
        out.append("")
    out.append(f"TOTAL: {round(grand)} pts")
    return "\n".join(out)


# ---------------------------------------------------------------- reference

# NOTE: this REFERENCE roster is a small illustrative sanity-check, not a
# live mirror of factions/imperial_regiments.json, which is still an
# UNTOUCHED, stale, d10-era roster -- re-costing the actual game's units
# against this rebuilt formula is separate, not-yet-started work (see
# path-to-playtest-2026-09-28.md). This reference roster exists only to
# confirm the formula itself still hits its own calibration target.
REFERENCE = {
    "name": "Reference roster (formula validation, not the real roster)",
    "units": [
        {
            "name": "Rifle Squad", "role": "LINE", "keyword": "Infantry", "size": 10,
            "profile": {"speed": 5, "mettle": 4, "evasion": 5, "armor": 4, "wounds": 1},
            "weapons": [
                {"name": "Rifle", "range": 18, "attacks": 1, "ap": 0, "damage": 1},
                {"name": "CCW", "range": "melee", "attacks": 1, "ap": 0, "damage": 1,
                 "traits": ["Unarmed"]},
            ],
            # NOTE: Massed Ranks is no longer a faction-wide signature trait
            # (it's Regiments' Infantry Platoon CORE bonus now, design-bible.md
            # SS8) -- left here only to confirm the mechanism still works, not
            # as a claim this unit still gets it automatically.
            "faction_trait": {"name": "Massed Ranks (example only)", "multiplier": 1.06, "min_size": 8},
        },
        {
            "name": "Heavy Weapons Team", "role": "SUPPORT", "keyword": "Infantry", "size": 1,
            "profile": {"speed": 5, "mettle": 4, "evasion": 5, "armor": 4, "wounds": 3},
            "weapons": [
                {"name": "Heavy Machine Gun", "range": 24, "attacks": 4, "ap": 2, "damage": 2,
                 "traits": ["Anti-Infantry", "Heavy", "Suppressing"]},
            ],
        },
        {
            "name": "Armored Personnel Carrier", "role": "SUPPORT", "keyword": "Vehicle", "size": 1,
            "profile": {"speed": 8, "mettle": 4, "evasion": 4, "armor": 6, "wounds": 8},
            "weapons": [
                {"name": "Light Machine Gun", "range": 18, "attacks": 4, "ap": 1, "damage": 1,
                 "traits": ["Anti-Infantry", "Suppressing", "Turret"]},
            ],
            "transport": 14,
        },
        {
            "name": "Armored Fighting Vehicle", "role": "ARMOR", "keyword": "Vehicle", "size": 1,
            "profile": {"speed": 8, "mettle": 4, "evasion": 4, "armor": 7, "wounds": 10},
            "weapons": [
                {"name": "Main Cannon", "range": 30, "attacks": 2, "ap": 6, "damage": 7,
                 "traits": ["Turret"]},
            ],
        },
    ],
}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = REFERENCE
    print(cost_roster(data))
