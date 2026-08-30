"""
Praxis Belli points calculator.

Implements the formula in design-bible.md section 11.

Usage:
    python points.py                 # cost the built-in reference roster
    python points.py roster.json     # cost a roster file
"""

import json
import sys

# ---------------------------------------------------------------- constants

# Currency scale. These two move together: multiplying both by the same factor
# rescales every cost in the game proportionally without altering any relative
# balance -- it is a pure unit conversion. Calibrated so that the anchor unit,
# a 10-model Rifle Squad with rifles and bayonets, lands on 100 points.
BASE_MODEL = 6.20         # a baseline grunt (EVA 6, ARM 4, SPD 5, MET 4, T 1)
BASE_WEAPON = 7.09        # scales weapon Value into points
REF_AP = 1                # reference AP used to normalise the Armor table
                          # (AP scale: 0 = assault rifle, 1 = magnum rifle,
                          #  2 = 20mm autocannon, 3 = 37mm, 4 = 57mm,
                          #  5 = 76mm, 6 = 88mm, 7 = 120mm sabot, 8 = railgun)

# High AP combined with volume of fire is the strongest thing a weapon can be,
# and pricing each linearly misses the interaction. Surcharge on the product.
AP_VOLUME_PREMIUM = 0.03

EVASION_CAP = 9           # above this the multiplier runs away

# Unit cost scales as N**SIZE_EXPONENT rather than linearly in model count,
# because the scarce resource in alternating activation is the activation, not
# the model. A 16-body mob delivering one activation is worth less per model
# than a 5-body team delivering one. Normalised so a 10-model squad is
# unchanged, which keeps the Rifle Squad calibration point at 100.
SIZE_EXPONENT = 0.85
SIZE_NORM = 10

# Trait modifiers. Every trait is multiplicative, on principle: a trait's
# value scales with how much the weapon already does (more hits landed means
# more suppression markers, more targets threatened by a blast, etc.), so its
# cost should scale the same way. A flat add doesn't -- it taxes a cheap
# weapon heavily and an expensive one barely at all, which is backwards.
#
# Individually tuning ~15 trait multipliers is exactly the kind of subjective,
# hard-to-defend pricing this system otherwise avoids. So traits are grouped
# into two bonus tiers and two restriction tiers, each a single fixed
# multiplier -- retuning the whole system is changing four numbers instead of
# fifteen, and reclassifying a trait is a one-line move between sets.
#
# Bonus tier is decided by whether the trait changes the SHAPE of the attack
# (major) or just improves the odds on an otherwise-normal shot (minor).
# Restriction tier is decided by whether it narrows WHAT can be targeted
# (minor) or WHEN the unit can act at all (major) -- Heavy sits alone in the
# major tier because "can't move and shoot" is a different category of cost
# than "can only shoot in one direction."
TRAIT_MINOR = 1.10
TRAIT_MAJOR = 1.30
RESTRICTION_MINOR = 0.90
RESTRICTION_MAJOR = 0.75

MINOR_TRAITS = {"accurate", "blast (s)", "engulf (s)", "suppressing", "turret", "pistol"}
MAJOR_TRAITS = {"linked-weapon", "blast (l)", "engulf (l)", "guided", "indirect"}
MINOR_RESTRICTIONS = {"coaxial", "frontal arc", "rear arc", "side arc"}
MAJOR_RESTRICTIONS = {"heavy"}

MULT_TRAITS = {
    **{t: TRAIT_MINOR for t in MINOR_TRAITS},
    **{t: TRAIT_MAJOR for t in MAJOR_TRAITS},
    **{t: RESTRICTION_MINOR for t in MINOR_RESTRICTIONS},
    **{t: RESTRICTION_MAJOR for t in MAJOR_RESTRICTIONS},
}

ANTI_MULT = 1.20          # per Anti-[Keyword] trait

# Special/named unit abilities (Priority Orders, Leadership Abilities,
# Triggered effects) are FLAT costs, not multipliers -- unlike a weapon trait
# or a stat, a standalone ability doesn't modify a base value the unit
# already has, so there's nothing principled to take a percentage of. Two
# tiers, same reasoning as the trait tiers: minor for a narrow or conditional
# edge, major for something that meaningfully changes how the unit survives
# or plays. Ratio (3x) matches the bonus-trait tier gap (1.10 vs 1.30).
ABILITY_MINOR = 5
ABILITY_MAJOR = 15
ABILITY_COST = {"minor": ABILITY_MINOR, "major": ABILITY_MAJOR}


# ---------------------------------------------------------------- primitives

def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def p_hit(evasion):
    """Chance an attack die hits a target with this Evasion."""
    return clamp((11 - evasion) / 10, 0.1, 0.9)


def p_damage(armor, ap=0):
    """
    Chance a hit converts to damage against this Armor, after AP.

    Armor may exceed 10. An unmodified 10 no longer auto-succeeds against such
    a target; it buys a second roll against (Armor - 10), cascading as needed.
    So ARM 17 vs AP 0 is 0.1 x 0.4 = 4% -- vanishingly unlikely, never
    impossible, and AP is the only real answer to it.
    """
    eff = armor - ap
    if eff <= 10:
        return clamp((11 - eff) / 10, 0.1, 0.9)
    return 0.1 * p_damage(eff - 10, 0)


# ---------------------------------------------------------------- model cost

def evasion_factor(evasion):
    """1/P(hit), normalised so Evasion 6 == 1.00."""
    if evasion > EVASION_CAP:
        raise ValueError(f"Evasion {evasion} exceeds the cap of {EVASION_CAP}")
    return (1 / p_hit(evasion)) / (1 / p_hit(6))


def armor_factor(armor):
    """1/P(damage) vs reference AP, normalised so Armor 4 == 1.00."""
    return (1 / p_damage(armor, REF_AP)) / (1 / p_damage(4, REF_AP))


def model_cost(speed, mettle, evasion, armor, toughness):
    e = evasion_factor(evasion)
    a = armor_factor(armor)
    s = 1 + (speed - 5) * 0.06
    m = 1 + (mettle - 4) * 0.06
    return BASE_MODEL * toughness * e * a * s * m


# --------------------------------------------------------------- weapon cost

def is_melee(rng):
    return isinstance(rng, str) and rng.strip().lower() in ("m", "melee")


def unarmed_value(attacks):
    """
    Value of the free unarmed attack every unit has: one attack per model,
    against the target's Evasion and Armor each raised by 1.

    Melee weapons are priced at their MARGIN over this. The baseline is
    universal, so by the same logic that makes TYPE and CATEGORY bundles free,
    it cannot be charged for.
    """
    soft = attacks * 0.4 * p_damage(4 + 1, 0) * 1
    hard = attacks * 0.5 * p_damage(8 + 1, 0) * 1
    return (soft + hard) / 2


def range_multiplier(rng):
    """rng is inches, or the string 'M'/'melee' for melee weapons."""
    if isinstance(rng, str) and rng.strip().lower() in ("m", "melee"):
        return 0.85
    return 0.6 + float(rng) / 30


def weapon_cost(rng, attacks, ap, damage, traits=()):
    traits = [t.strip().lower() for t in traits]

    # Fists. Every model in the game carries one, so it is universal and
    # therefore free -- the same logic that makes TYPE and CATEGORY bundles
    # free. It exists as a real profile rather than an abstract rule so that
    # everything referring to "a melee weapon" resolves without special cases.
    if "unarmed" in traits:
        return 0.0

    # Two reference targets: soft (EVA 6 / ARM 4) and hard (EVA 5 / ARM 8).
    p_soft = p_damage(4, ap)
    p_hard = p_damage(8, ap)

    # Overkill cap: excess Damage is wasted on low-Toughness targets.
    soft = attacks * 0.5 * p_soft * min(damage, 2)
    hard = attacks * 0.6 * p_hard * damage
    value = (soft + hard) / 2

    # Every unit can already fight unarmed for free, so a melee weapon is only
    # worth the improvement it represents over that baseline.
    if is_melee(rng):
        value = max(value - unarmed_value(attacks), 0.05 * value)

    cost = BASE_WEAPON * value * range_multiplier(rng)

    # Penetration x volume premium. A weapon that is both piercing and
    # high-volume is the best thing on the table; pricing each term linearly
    # undercharges the combination badly.
    cost *= 1 + attacks * ap * AP_VOLUME_PREMIUM

    for t in traits:
        if t.startswith("anti-"):
            cost *= ANTI_MULT
        elif t in MULT_TRAITS:
            cost *= MULT_TRAITS[t]

    return max(cost, 1.0)


def transport_cost(capacity):
    return capacity * 0.439          # scaled with the currency, see BASE_MODEL


def size_factor(size):
    """
    Per-model multiplier from sublinear scaling in unit size.

    Single models pay a premium (they deliver a full activation and never
    degrade); big units get a discount (one activation, overkill waste,
    coherency drag). Normalised so size 10 == 1.00.
    """
    return (size / SIZE_NORM) ** (SIZE_EXPONENT - 1)


# ------------------------------------------------------------------ costing

def cost_unit(unit):
    """Cost one unit dict. Returns (total, breakdown_lines)."""
    lines = []
    p = unit["profile"]
    size = unit.get("size", 1)

    per_model = model_cost(p["speed"], p["mettle"], p["evasion"],
                           p["armor"], p["toughness"])
    chassis = per_model * size
    lines.append(f"    chassis  {size} x {per_model:6.1f} = {chassis:7.1f}")

    total = chassis

    for w in unit.get("weapons", []):
        n = w.get("count", size)
        each = weapon_cost(w["range"], w["attacks"], w["ap"],
                           w["damage"], w.get("traits", []))
        sub = each * n
        traits = ", ".join(w.get("traits", [])) or "-"
        lines.append(f"    {w['name']:<22} {n} x {each:6.1f} = {sub:7.1f}   [{traits}]")
        total += sub

    if "transport" in unit:
        t = transport_cost(unit["transport"])
        lines.append(f"    Transport({unit['transport']}){'':<11} {t:20.1f}")
        total += t

    # Sublinear scaling in unit size, applied to the whole fighting profile.
    sf = size_factor(size)
    if abs(sf - 1.0) > 0.005:
        scaled = total * sf
        lines.append(f"    size x{sf:.3f} (n={size}){'':<6} {scaled - total:+20.1f}")
        total = scaled

    # Faction signature trait. Hand-priced multiplier on the unit total; these
    # are the least-defensible numbers in the system and the first thing
    # playtesting should attack.
    ft = unit.get("faction_trait")
    if ft and size >= ft.get("min_size", 0):
        mult = ft.get("multiplier", 1.0)
        scaled = total * mult
        lines.append(
            f"    {ft['name']:<22} x{mult:.2f}{'':<12} {scaled - total:+8.1f}   [faction]"
        )
        total = scaled

    # Per-unit trait multipliers (Conscript, and anything else that modifies
    # what a unit is worth rather than what it can do).
    for mod in unit.get("modifiers", []):
        mult = mod.get("multiplier", 1.0)
        scaled = total * mult
        lines.append(
            f"    {mod['name']:<22} x{mult:.2f}{'':<12} {scaled - total:+8.1f}   [trait]"
        )
        total = scaled

    # Special/named abilities are flat and sit outside the size curve -- they
    # usually attach to one model (a leader's Priority Order), not the squad.
    for extra in unit.get("extras", []):
        tier = extra.get("tier")
        cost = ABILITY_COST[tier] if tier else extra["cost"]
        label = tier or "hand-priced"
        lines.append(f"    {extra['name']:<22} {cost:26.1f}   [{label}]")
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
        tags = "/".join(filter(None, [unit.get("category"), unit.get("type")]))
        out.append(f"{unit['name']}  [{tags}]  -> {round(total)} pts")
        out.extend(lines)
        out.append("")
    out.append(f"TOTAL: {round(grand)} pts")
    return "\n".join(out)


# ---------------------------------------------------------------- reference

REFERENCE = {
    "name": "Reference roster (validation)",
    "units": [
        {
            "name": "Rifle Squad", "category": "LINE", "type": "Infantry", "size": 10,
            "profile": {"speed": 5, "mettle": 4, "evasion": 6, "armor": 4, "toughness": 1},
            "weapons": [
                {"name": "Rifle", "range": 18, "attacks": 1, "ap": 1, "damage": 1},
            ],
        },
        {
            "name": "Heavy Weapons Team", "category": "SUPPORT", "type": "Infantry", "size": 1,
            "profile": {"speed": 5, "mettle": 4, "evasion": 6, "armor": 4, "toughness": 3},
            "weapons": [
                {"name": "Heavy Machine Gun", "range": 24, "attacks": 4, "ap": 3, "damage": 2,
                 "traits": ["Anti-Infantry", "Heavy", "Suppressing"]},
            ],
        },
        {
            "name": "Armored Personnel Carrier", "category": "SUPPORT", "type": "Vehicle", "size": 1,
            "profile": {"speed": 8, "mettle": 4, "evasion": 5, "armor": 6, "toughness": 8},
            "weapons": [
                {"name": "Light Machine Gun", "range": 18, "attacks": 4, "ap": 1, "damage": 1,
                 "traits": ["Anti-Infantry", "Suppressing", "Turret"]},
            ],
            "transport": 14,
        },
        {
            "name": "Armored Fighting Vehicle", "category": "ARMOR", "type": "Vehicle", "size": 1,
            "profile": {"speed": 8, "mettle": 4, "evasion": 4, "armor": 7, "toughness": 10},
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
