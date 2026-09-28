# Praxis Belli — Design Bible

**Status:** v0.5-in-progress — converting the core dice engine from d10 to d6 for component accessibility (most players own dozens of d6, far fewer own enough d10 to roll a whole squad's attacks at once). This is a breaking change to the probability foundation everything else is built on, being carried out one section at a time; sections not yet touched still describe the d10-era numbers and are marked as such. `reference.html` (the formatted twin) has **not** been updated yet and will drift out of sync until a dedicated pass syncs it — treat this document as authoritative during the conversion.

**Source of truth — two modes, not one:** while actively building or revising stats and profiles together, this document and `points.py`/`factions/*.json` lead — that's what a design session *is*. Outside of that, **NewRecruit is the default source of truth**: `PraxisBelli.gst` and the `.cat` files in `C:\Users\darry\Documents\NewRecruit\data\PraxisBelli\` reflect whatever was last hand-edited there directly, which may not match what's written here. When the two disagree, that's a conflict to surface and resolve, not something to silently overwrite in either direction. The older `Documents\NewRecruit\data\Praxis Belli\` folder (with a space) is superseded regardless of either mode; it holds an earlier `Praxis Belli.gst` plus Oathbreaker Legions / Oathkeeper Cohorts catalogues on a different game system ID.

**Design lineage:** *Marcher: EAW* (Platoon frame, Transports, attacker-rolled Evasion/Armor), *Ravaged Star* (d10 roll-over engine, 1-fails/10-succeeds, the Damage stat, "Shaken"), and *Warmachine MkIV* (facings and arcs, model-count transports).

### v0.5 Decision Queue — decided, not yet written into the sections below

Snapshot of the latest design decisions as of 2026-09-28. **Already applied in this document:** the d6 conversion (§3, the §5 Mettle-check formula, `Guided`). **Decided but not yet applied** — where this list and an older section below disagree, this list wins. Suggested order: Role/Keyword → points formula (which needs both the die and the Role/Keyword change); Morale and Formations are independent and can run in parallel. Legacy snapshots of every doc as they stood before this work are saved alongside as `*_legacy.*`.

1. **Role + Keywords replace TYPE/CATEGORY** (rewrites §7; knock-ons in §8 Platoons, §10 Transports' "takes the payload's CATEGORY" rule, and the trait glossary).
   - A unit has one **Role** — the force-org slot it fills. Role is a list-building label only and grants no rules.
   - A unit has any number of **Keywords**. Keywords do nothing on their own; they exist to sharpen targeting (`Anti-[Keyword]`, "choose a friendly [X] unit to…") and to come bundled with traits. *Unconfirmed reading of "bundled with traits": a design-time convenience when building a unit, not an automatic runtime grant — confirm before writing §7.*
   - Everything TYPE/CATEGORY used to grant automatically (Bulwark, Hardpoints, Leadership Aura, Boots on the Ground, Spotter/Camouflaged/All-Terrain, Brutal Assault, Where We're Needed, Entrenched, Run Them Through, Armored Front, Terrifying, Flying/Soaring Above, Trailor/Emplaced Weapon) becomes an individually assigned **Trait** and must now be *priced* (Major/Minor flat tiers, §11 Step 5) because it is no longer free. This also closes the old gap where COMMAND's Leadership Aura had positional value but was priced as free.
   - `Anti-[Keyword]` generalizes to "any keyword" instead of the fixed 12-label list.
2. **Morale redesign** (§5). Goal: morale is a real lever players can pull, without a doom spiral.
   - Cut "a worsened Mettle" from **Shaken** — it stacked with the marker-count penalty on the same check. Shaken becomes −1 Evasion / −1 Armor only; suppression markers alone carry the rising difficulty.
   - Add a **Leader trait** that strips suppression markers from its own unit or from allies in an aura (protect your officers, hunt theirs).
   - Suppression-immunity traits (`Fearless`, `Undaunted (X)`, `Mindless`'s immunity clause) become rare, expensive, and faction-signature rather than a common menu option; reprice them accordingly.
   - The track and math stay universal across every faction (no per-faction morale subsystems). Factions differ in *access* to the rare immunity traits, not in rules. Faction flavor may rename the steps without changing them.
3. **Formations / CORE** (rewrites §8's Named Platoons). Choosing a Formation designates a **CORE** Role/Keyword. *Only* CORE units get the Formation's passive bonus, and that Role's slot cap is raised. One uniform template replaces the bespoke Platoon Abilities, which also settles the undesigned ARMOR and SUPPORT ones. **Not yet decided:** the actual bonus each Role receives.
4. **Points formula rebuild** (rewrites §11 in full).
   - Recompute every probability table for d6 (a rebuild, not a reskin).
   - Calibration anchor: a 10-model "G.I."-equivalent rifle squad = **exactly 100 points**, carrying rifles and `CCW` only — **no bayonets by default**.
   - **`CCW`** (Close Combat Weapon) replaces `Fists` as the free universal melee profile (§4). It is named to avoid implying biology. Real melee weapons are priced at their margin over CCW, as Fists worked before; the derived "69% of a Bayonet" figure in §4 must be recomputed.
   - Target cost split for that squad: about **80% model / 20% weapons** — weapons cheaper, units carry most of the cost.
   - Add an **AP overkill cap** (see §3, "Armor's floor") mirroring the existing Damage overkill cap.
   - Price the traits that used to be free bundles (item 1) and recalibrate the Mettle value range for d6.
5. **Modifier policy.** Ordinary ±1 modifiers are fine on d6. Any modifier of ±2 or more should be written as a floor or static target number rather than a subtraction (as done for `Guided` and range bands).
6. **Remaining d10-era dice and thresholds outside the attack/Mettle engine** — found by search, not yet converted, and some need a design decision rather than a notation swap: `Dangerous` terrain (rolls d10, 4+ passes); `Blast` scatter (1d5" / 1d10"); `Regeneration` and `Combat Medic` (1d5 wounds restored); `Shrug (X)` ("roll a d10… unmodified 10 always succeeds"); `Extra Hits (X)` and `Critical (X)` (default X = 10 — no longer reachable); `Critical Weakspot` (keyed to an unmodified 10); `Undaunted (X)` (Repentia at 7+ — **impossible on a d6**); the "Armor 10/11+" rows of the §11 cost table; and the "Critical Hit" wording anywhere else it says 10.

**Raised but not decided:** vehicle squadrons (fielding 2–3 same-chassis vehicles as one multi-model unit to escape the single-model Size Factor surcharge, Flames-of-War style); a larger standard game (roughly a 3000-point 10th-edition-40k equivalent on a 6'×4' table) and possibly a smaller model scale — neither changes the ruleset now, but a 6'×4' table needs §9's terrain-density numbers recalculated, and a smaller scale strains §6's true-line-of-sight rule.

#### Resolved 2026-09-28 (design conversation) — decided, not yet written into the sections below

**Decided:**

- **Role vs Keywords.** Every unit's Role (one, the force-org slot) must be re-tuned to reflect what the unit is *expected to do on the battlefield*. Everything else about the unit is expressed as **Keywords**. Keywords come in two kinds: those that are simply *referenced* by other rules' text (RECON — by `Guided`, `Spotter`, `Indirect`; and any `Anti-[Keyword]`), and those the **core rules** attach effects to automatically (VEHICLE, INFANTRY…). Whether a given keyword is also wired into the `.cat`/`.gst` is a per-keyword call.
- **Objectives.** The INFANTRY keyword is written in the core rules as "does not spend an action to claim an objective"; **any other unit may claim, but must spend an action to do so.** *(Consequence to check: this retires §9.1's "vehicles, monsters and aerials can only contest, never score" — see Open Questions below.)*
- **Evasion.** Anchored by what the unit *is* (Keywords), as TYPE was, but with finer distinctions available (e.g. a MECH keyword). **Standard infantry Evasion 5+** — leaves room for cover to matter on default squads; units with baked-in Evasion 6+ stand out and must be answered with the right tools when dug in or stacked with modifiers. The Rifle Squad anchor therefore moves from Evasion 6 to Evasion 5 (recalibrate §0 and §11).
- **AP / Armor scale.** AP is 0–X with **no cap at 4**. Armor may reach ~10. AP lowers the Wound Roll target; **AP can only reduce a target to 2+** (this floor *is* the AP overkill cap the queue asked for). AP0 weapons are nearly useless against heavy armor by design; heavy armor demands heavy guns. Dedicated anti-tank weapons carry high Damage so their limited shots count.
- **Terminology.** Rules text now says **Attack Roll** (the roll against Evasion) and **Wound Roll** (the roll against Armor). A natural 1 never wounds. How a Wound/Attack Roll target of **7+** is handled must be deliberate — see Proposed below.
- **Range bands.** Close / Effective / Long, applied in §3 (Long extends to 1.5× the Range; 2× was the alternative).
- **CORE is defined per Formation, per faction.** Not every faction gets every Formation (e.g. Saints barely field RECON, so need no RECON Formation). Bonuses are deliberately asymmetric and should reinforce a faction's strength or slightly lessen one of its weaknesses (illustrations, not decisions: Regiments' infantry Formation gets a massed-fire benefit; Oathkeepers' infantry Formation gets a pre-game redeploy).
- **Charges** roll d6 + Speed.
- **`Iron Horizon`** is a dead name; that project was abandoned in favour of Praxis Belli. `ProjectSummary.md` rewritten this pass to drop it.
- **`Tithe of Skulls`** (Wrathbound Oathbreakers `.cat`) is kept but needs simplification — see Round 2 below.

**Proposed, awaiting confirmation:**

- **Morale on 2d6**, additive and higher-is-better: `2d6 + Mettle − suppression markers ≥ 10`, with natural 2 always failing and natural 12 always passing. Rationale: on d6 every Mettle from 4 to 7 passed at 83% with 0 markers, so Mettle stopped meaning anything until markers accumulated. **Recommended and provisionally locked at TN 10** (Round 2) — see below.

#### Round 2 — 2026-09-28 (later the same day)

**Decided:**

- **Targets of 7+ — keep the legacy cascade** (natural 6, then re-roll against *target − 6*), i.e. §3 "Armor above 6" is unchanged. The *target − 5* ladder proposed above is **shelved, not adopted** — kept below only as a documented alternative in case the legacy cascade proves to need it. It's suspected to matter only for low-AP weapons vs. high-Armor targets, which may be rare enough not to need solving at all. Two other directions to weigh before touching the cascade again:
  - Design stat lines so they land on a "step" deliberately, and accept it: e.g. an up-armored-Humvee-equivalent sitting at **Armor 8** where **AP1 simply does nothing** is a fact about the vehicle, not a curve to smooth.
  - *(Shelved alternative, for reference only)* natural 6, then re-roll against *target − 5*: 6+ = 16.7%, 7+ = 13.9%, 8+ = 11.1%, 9+ = 8.3%, 10+ = 5.6%, 11+ = 2.8% — a smooth ladder, vs. the legacy cascade's 7+ and 8+ landing on the same 13.9%.
- **`Anti-[Keyword]`, intent confirmed.** The point is a **cheaper way to build a specific-target tool** than raising AP, Attacks, or Damage generally — trading weapon cost for narrowed generalization (useless against anything but the matching keyword) rather than trading it for raw power. Keep the ×2-hits mechanic; price it **target-bucket-aware** (double only the matching soft/hard reference term in the formula, not a flat multiplier) once §11 is rebuilt, so it functions as the discount it's meant to be rather than a flat tax. May turn out to fall out of the formula for free — revisit once the rebuild lands.
- **Morale TN 10 — confirmed.** It ties directly to the Rifle Squad's own Mettle 4: 0 markers = 72%, then 58/42/28/17% as markers stack — a real, crackable lever with no saturation. Mettle 1–2 (Conscript-tier) genuinely struggles (28%/42% unsuppressed); Mettle 7 (the Commander) is strong but not automatic even clean (97%) and still degrades under pressure (58% at 4 markers). TN 9 or 11 push the anchor to 83%/58% respectively — 10 is the better fit. Locking it; 2d6 also opens room to widen the Mettle spread itself during the roster recalibration pass, if a finer gradient is wanted later.
- **Claiming objectives, non-INFANTRY.** Closes the loophole where a unit already parked on an objective could spend one action to Claim and its other to Shoot, paying nothing real: **Claim, for any unit without the INFANTRY keyword, is taken as that unit's Combat action** (it cannot also Shoot or Fight in the same activation) — it may still Move. A vehicle *can* sit on an objective and claim it, but only by giving up its firepower that activation, which is the intended "horribly inefficient" cost. Preserves the spirit of the old "armor denies, doesn't easily hold" lever even though vehicles can now technically score.
- **Keywords carry no cost by default.** A keyword itself is never priced; only the rule(s) it brings (if any) are priced, at whatever tier that rule already costs.
- **No more rule-bundling as house style.** Prefer smaller, individually named, recycled rules that read the same everywhere over faction-exclusive combo traits. Applied immediately to two rules:
  - **`Tithe of Skulls` unbundled.** Drops its "ignores suppression on Morale tests" clause (redundant — `Fearless` already covers Marine-chassis Wrathful Oathbreaker units, and the faction identity is explicit that Cultists/Spawn don't get it either way). Keeps the forced-charge clause. The post-kill reward becomes flat `Extra Hits` (see next bullet), not a configurable threshold.
  - **`Extra Hits` loses its configurable `(X)`.** Always keyed to a natural 6 — the same trigger as the universal Critical Hit rule, no longer stackable down to a lower threshold like 7+ or 9+. Every current citation of a specific X (Fanatical Sisters' Heavy Ripsaw Sword at 10, Sister Defensors' Anointed Halberd at 10, Ascendant Ripsaw Sword at 9+, `Tithe of Skulls`' own proposed 8+) needs to drop the number.
- **Standard game scale is open again.** 1000 points is no longer assumed — 2000 or 3000 is the likely target, to be decided once the points formula lands. Every "1000-point" / "2 Platoons" reference (Principle 0, §8, §11) is stale pending that call; don't edit them yet.

**Open, unresolved:**

1. **Resolved (Round 3):** `Massed Ranks` *becomes* Regiments' Infantry-anchored Formation's CORE bonus, rather than sitting alongside a separately invented one. It stops being granted faction-wide to any 8+-model unit and instead applies only to CORE-tagged, Infantry-keyword units within that specific Formation (same internal "8+ models" condition on the unit itself, unchanged) — closing the overlap concern outright, since there's no longer a second, distinct bonus to overlap with.
2. **New, opened by the above:** `Massed Ranks` was also Imperial Regiments' faction-wide *signature trait* (one per faction, per `faction-identity.md`'s design rule). Moving it into a Formation-gated CORE bonus vacates that role — **Regiments needs a new faction signature trait.** Deliberately deferred, not designed now.

#### Round 3 — 2026-09-28 (same day, following the Critical/Anti-X discussion)

**Decided:**

- **`Critical (X)` is retired entirely** — not merged into anything, just gone. It was briefly floated as a universal rule, which was a misreading on my part (it was always meant as an optional, per-weapon trait, same as `Overcharge` or `Shrug`, so the "it would break AP0-vs-heavy-armor for everyone" objection didn't actually apply). Retired anyway, on its own merits: `Anti-[Keyword]`'s new shape (below) already delivers the "hits hard on a hot roll against the right target" feeling it was meant to provide, so it's redundant rather than needed. A precision/sniper-flavored weapon that wants a crit identity takes an `Anti-[Keyword]` (Anti-Infantry, etc.) instead of a bespoke trait — confirmed as a real, working alternative: an Anti-Materiel Rifle can be built either by baking a higher AP straight into its profile, or by taking one or more `Anti-[Keyword]` tags at a lower base AP/Damage. Two legitimate paths to the same "beats one specific thing" niche, which is exactly the intent `Anti-[Keyword]` was designed to serve.
- **`Anti-[Keyword]`, final shape, replacing the ×2-hits rule entirely:** *"Whenever this weapon's Attack Roll against a target with [Keyword] is an unmodified 6, it immediately deals its Damage value to that target's wounds — no Wound Roll made for this portion, so it bypasses Armor and AP entirely (still reduced by flat damage-mitigation like `Bulwark`, and nullified the same as any other Anti-[Keyword] effect by `Negates ([Keyword])`). The attack then resolves normally on top of that — the Attack Roll was already a hit (natural 6 always hits), so it still gets its own ordinary Wound Roll exactly as any other successful hit would."* One behavior, additive, no configurable `X` — the free hit is always worth the weapon's own Damage stat, so heavier weapons naturally get a bigger bonus without a second number to balance. This is chosen over three other candidate shapes (doubling the number of wound rolls on the crit; doubling Damage only if the accompanying roll also succeeds; auto-succeeding the roll with no second hit on top) specifically because it's the only one of the four that guarantees a crit against the right target is never a dud — the other three can still whiff to zero on the very roll that was supposed to feel explosive.
- **Spillover — correction to the note above: it isn't retired, it was never Anti-X-specific to begin with.** A natural 6 against a matching keyword now produces *two distinct hits* — the guaranteed free one (dealt instantly) and the "real" one (still resolved normally, its own Attack Roll already a success). Each hit affects one model by default, the same rule that already governs any weapon with Attacks > 1 or `Extra Hits`. Since these are two separate hits, they're already free to land on different models in the target unit via that existing allocation order — no bespoke clause needed on `Anti-[Keyword]`'s own text, because the behavior was never a special exception, just an ordinary case of the standing one-hit-per-model rule.
- **`Extra Hits` doesn't stack with other traits that also trigger off an unmodified 6, on the same Attack Roll.** Written as a general non-stacking clause on `Extra Hits` itself, not an enumerated list — there's no fixed count of "on a 6" traits yet, and a list would need updating every time a new one is built. "Doesn't stack" means they don't *compound* — they aren't mutually exclusive. If a weapon somehow carries both `Extra Hits` and a triggered-on-6 effect like `Anti-[Keyword]`'s free hit, a natural 6 triggers **both in full** (the extra hit *and* the guaranteed free hit), each resolving as its own separate, un-multiplied instance — neither amplifies the other.

**Housekeeping:** `ProjectSummary.md` predates all of this — it still says "Iron Horizon" and a 2000-point target game, against this document's Praxis Belli name and 1000-point target. `reference.html`, `faction-identity.md`, `points.py`, `build_cat.py`, and `factions/imperial_regiments.json` still reflect the d10-era design.

---

## Design Principles

### 0. The Rifle Squad is the unit of account

**This game is balanced around a regular rifleman squad. Not around elites.**

Ten bodies, Toughness 1, Armor 4, Evasion 6, Speed 5, Mettle 4, ~100 points. That is the reference unit, the formula's calibration anchor, and the mental model for army size — a 1000-point list is *about ten rifle squads' worth of stuff*.

Three rules follow, and they are anti-spiral rules:

1. **Every mechanic is evaluated by what it does to a rifle squad.** If a rule is neutral or confusing for line infantry and only makes sense for a five-model elite squad, it is the wrong rule.
2. **When an elite unit needs a new subsystem to function, the elite is wrong — not the game.** Elite units get better *stats* and better *weapons*, both of which the points formula already prices. They do not get compensation mechanics. If five Oathkeepers underperform ten riflemen at the same cost, their stat line is wrong, or their price is.
3. **New systems must justify themselves for the common case.** A rule introduced to solve an elite faction's problem has to also earn its place in a mirror match of line infantry, or it does not go in.

The failure mode this guards against is real and it compounds: each fix for an exceptional unit adds a subsystem, the subsystems interact, and the game ends up complicated in service of the units *fewest* players field.

### Resolved conventions

- **Mettle is additive and higher-is-better** — `d6 + Mettle ≥ 6 + suppression markers` (re-anchored from d10; see §3). Every stat on the card now reads "bigger is better."
- **The attacker rolls both** the to-hit check and the damage check. The `.gst`'s older "defensive saves" phrasing on Anti-[Keyword] rules is legacy wording; the mechanics are unchanged either way, but higher Armor can only mean *tougher* if the attacker is the one rolling against it.

---

## 1. Activation & Actions

Alternating activation, unit by unit. Round ends once every unit has activated.

### Pass Tokens

Only the player with **fewer units** receives them, equal to the delta between the two unit counts. No other source of passes.

When it is your turn to activate and you have no unit you wish to activate, spend a Pass Token instead. **Spending a Pass Token lets one friendly unit that has not yet activated make a free half-Move.** That unit is not considered activated and may still act normally later in the round.

**Why they do something:** an outnumbered army's real deficit is not tempo — pass tokens already keep the round even in count — it is **board coverage**. Six units cannot be in as many places as twelve, and since only infantry can claim objectives, being outnumbered means being out-positioned. Repositioning is therefore the exact compensation the deficit calls for, and it turns "I have fewer units" from pure disadvantage into a different way of playing: fewer pieces, moved more often.

This deliberately avoids becoming a resource economy or a reaction system. A Pass Token buys movement and nothing else.

**2 actions per activation**, baseline. Taken in any order, each used once per activation (special rules can break this).

Common actions: **Move**, **Shoot**, **Fight**, **Rally** (remove all suppression markers from this unit), **Claim** (take an objective; LINE units do this for free). Some units get a free bonus action as a named exception — not a universal system.

No general reaction economy. Triggered abilities are written per-unit as exceptions.

## 2. Movement & Formation

No coherency stat. Move the leader model by its **Speed** stat, then place the rest of the unit within 2" of the leader, or within 2" of two models that are each within 2" of the leader (Warmachine-style reset — formation "resets" every time the unit moves).

Engagement range: 1" baseline, extendable by weapon or trait.

## 3. The Dice Engine

**Every check is roll-over on a d6: meet or exceed the target number to succeed.** *(Converted from d10 — see the version note at the top of this document for why.)*

**Dice floor/ceiling, universal:** an unmodified **1 always fails**; an unmodified **6 always succeeds**. "Unmodified" means the raw face physically shown on the die — this check happens before any modifier is applied, whether that modifier lands on the target number (most traits) or directly on the roll itself (range bands, below). A natural 6 always succeeds even after a −1 range penalty; a natural 1 always fails even after a +1.

### The attack sequence

1. **To-hit** — roll d6 per attack die against the target's **Evasion**. Total dice = weapon's Attacks × models firing.
2. **Damage check** — each hit rolls again against the target's **Armor**, after **AP** is subtracted. Each success inflicts the weapon's **Damage** value in wounds against the target's **Toughness**.

**Critical Hit** — a hit roll of an unmodified 6 is a Critical Hit. On its own this changes nothing beyond the success it already represents under the floor/ceiling rule above — it's a named hook, not a bonus, and exists purely so traits can key off it (`Extra Hits (X)`, `Critical (X)`, `Negates (Critical Hits)`; see glossary). Deliberately no baseline effect for anyone: a universal "natural 6s also auto-wound" rule would let every weapon in the game ignore the AP scale on a flat ~17% chance regardless of how mismatched it is against the target's Armor, which undermines AP's whole job as "the only real answer to heavy armor" (below) — keeping the bonus trait-gated means only weapons built for that identity get it.

Higher Evasion = harder to hit. Higher Armor = harder to damage.

There is no attacker-side accuracy stat. To-hit difficulty is entirely defender-side; attacker differentiation comes from traits, rerolls, and Anti-[Keyword] weapons.

### Evasion — templated by TYPE, not freely tuned

d6 only offers five meaningfully distinct values (2 through 6), which isn't enough room for the fine per-unit tuning the old d10 curve allowed. Evasion is now assigned by broad TYPE template rather than hand-picked per unit:

| TYPE | Evasion | Hit chance |
|---|---|---|
| Heavy Vehicle | 2–3 | 83% / 67% |
| Light Vehicle | 3–4 | 67% / 50% |
| Infantry (baseline) | 5 | 33% |
| Elite / dedicated dodge specialists | 6 | 17% |

Evasion above 6 is reachable only through modifier stacking, never as a base value, and cascades exactly like Armor above 6 (below) once it happens. This is rare enough in practice that a known quirk of the cascade — Evasion 7 and 8 land on the *identical* ~14% chance (both reduce to "a natural 6, then anything but a natural 1") — isn't worth solving for. The same quirk is a real problem for Armor, immediately below, because AP makes it come up constantly rather than rarely.

**Veterancy no longer differentiates through Evasion.** A veteran and a rookie of the same TYPE share the same defensive template; the gap between them has to come from Mettle, Armor, Speed, Toughness, equipment, and traits instead. *(The exact Mettle values a roster should span under the new die haven't been recalibrated yet — flagged in Open Threads.)*

### Armor above 6

Armor is **not capped at 6**. When a target's Armor after AP exceeds 6, an unmodified 6 no longer succeeds automatically — instead it buys a **second roll** against `Armor − 6`, cascading again if that also exceeds 6.

A hull at Armor 9 struck by an AP 0 weapon needs a 6, then a 3+: `1/6 × 4/6 ≈ 11%`. The same hull struck by an AP 3 weapon is rolling against a flat effective Armor of 6 — a straight `1/6 ≈ 17%`. Higher AP still means a meaningfully better chance to damage, exactly as intended; the curve continues smoothly instead of hitting a wall.

*(Mechanic unchanged from the d10 version — Marcher's original inspiration — just re-anchored to the smaller die.)*

### Armor's floor, and AP overkill — flagged, not yet solved

The same "two different numbers land on the identical probability" quirk that's harmless at Evasion's rare ceiling is a real problem at Armor's **floor**, and it isn't rare: once AP has dropped a target's effective Armor to 1 or below, **any further AP is wasted against that target** — Armor 1, 0, and −1 all resolve identically. Because AP subtracts from Armor on every single attack, this happens in ordinary play constantly, not as an edge case. The weapon-cost formula already solves the mirror-image problem for Damage (`min(Damage, 2)` against soft targets, §11) — AP likely needs the same kind of overkill cap. **Not designed yet; carried into Open Threads below so it isn't lost when §11 gets rebuilt.**

### The AP scale (draft — needs playtesting-anchored calibration)

AP's range compresses along with the die: each point now does proportionally more work against a 5-step Armor range than it did against d10's wider one, so the old 0–8 scale is oversized. Draft compression to 0–4 below — the real-world reference pairings are a first-pass placeholder, not a calibrated result:

| AP | Reference |
|---|---|
| **0** | Modern assault rifle |
| **1** | Magnum cartridge / 20mm autocannon |
| **2** | WWII 37mm / 57mm |
| **3** | 76mm / 88mm |
| **4** | Modern 120mm sabot / railgun |

**Most infantry weapons sit at AP 0.** Penetration is bought through heavy weapon teams and vehicles, not carried by line infantry — a large part of why combined arms is mandatory rather than merely encouraged.

### Range bands

A weapon's printed **Range** is the middle of three bands, each measured from the firing model. Range modifies the **Attack Roll itself**, not the target number (a deliberate change from the d10 version — see the floor/ceiling note above for how the two interact):

| Band | Distance | Attack Roll |
|---|---|---|
| **Close Range** | within half the weapon's Range | **+1** |
| **Effective Range** | more than half, up to the weapon's Range | +0 |
| **Long Range** | beyond the weapon's Range, up to **1.5×** the Range | **−1** |

Beyond 1.5× the Range, the weapon cannot target. *(1.5× rather than 2×: it makes the three bands equal thirds of the weapon's reach, and it stops a 24" weapon from covering an entire 4'×4' board. Flagged for playtesting.)* `Accurate` removes the Long Range penalty only — it does not remove the Close Range bonus.

## 4. Melee

**Fire into melee:** allowed. A missed shot against an engaged target instead hits an ally in that fight — the opponent chooses which model eats the miss.

**Fire out of melee:** not allowed — except **Pistol**, which may make a ranged attack while its bearer is engaged, but only against an enemy unit it is engaged with.

### Fists

**Every model carries this weapon profile whether or not it also has a melee weapon.** Written up as a real profile rather than an abstract rule, so anything that references "a melee weapon" resolves without a special case:

> `Fists | Melee | Attacks 1 | AP 0 | Damage 1 | Traits: Fixed, Unarmed`
>
> **Unarmed** — this weapon's target has its Evasion and Armor each increased by 1 for that attack.

Nothing in the game is ever helpless in melee — it is simply bad at it. Against a baseline target Fists are about **69%** as effective as a Bayonet, so a real melee weapon is a genuine upgrade rather than the difference between fighting and not.

> **Pricing consequence:** because every model has Fists, it is **free** — the same logic that makes TYPE and CATEGORY bundles free. Real melee weapons are priced at their **margin over Fists**, not their absolute value. Skipping this would charge every model twice for a capability it already had.

## 5. Morale — Determined → Shaken → Frozen → Routing

### The Mettle check

```
Roll d6 + Mettle.  Pass if the total ≥ 6 + suppression markers held.
```

Higher Mettle is better, like every other stat on the card. A unit with Mettle 4 holding two markers needs a 4+ *(re-anchored from d10; the actual Mettle values a roster should span under the new die still need a recalibration pass — see Open Threads)*.

- **Pass** — remove **one** suppression marker.
- **Fail** — step **up** one level on the track.

**Check timing:** at the start of a unit's activation if it holds any markers, or immediately when an effect forces one.

**Naming note:** this specific check — the one that can step a unit up the morale track — is a **Morale test**. The same underlying roll (d6 + Mettle vs. a target number) is reused for other, unrelated triggered effects (`Rallying Cry`, `Combat Medic`, `Divine Favor`, etc.); those are **Mettle checks**, not Morale tests. The distinction matters because some traits (`Mindless`, `Undaunted (X)`) specifically reference Morale tests only — they don't touch a unit's other Mettle-gated abilities.

### Suppression markers

Dealt by weapons and effects (see **Suppressing**). **Markers persist until removed.** They do not clear at end of round.

Three ways to be rid of them, none punishing:

| Method | Removes |
|---|---|
| Passing a Mettle check | 1 marker |
| The **Rally** action | *all* markers on this unit |
| Specific effects (e.g. *Hold Fast*) | as written |

**Rally** is an action like Move, Shoot, or Fight — one of a unit's two.

### Recovery

> A unit steps **down** one level at the end of its activation **only if it holds no suppression markers.**

This single clause is what makes the whole morale system work, and it is worth understanding why.

**The problem it fixes:** with automatic recovery, a unit checked at the start of its activation, went Shaken, acted, and recovered at the end of that same activation. But Shaken's penalties are −1 Evasion and −1 Armor, which only bite *when being attacked* — during the opponent's activations. With no reaction economy, the defensive half of the penalty could essentially never apply. Frozen was near-unreachable for the same reason. The entire track was ornamental.

**What it creates instead:** a genuine decision, every activation, for every suppressed unit.

- **Rally** — spend half your activation clearing markers, recover at end of turn, act at reduced capacity.
- **Don't** — take both actions, but keep the markers, stay Shaken through the opponent's turn at −1 Evasion / −1 Armor, and check again next activation at the same penalty. Fail twice and you are Frozen.

That is what suppressing fire is *supposed* to mean: it costs the target tempo, or it costs them safety. **The real price of suppression is actions, not damage** — which is also why `Suppressing` deserves its points.

### The track

| Level | Effect |
|---|---|
| **Determined** | Baseline. |
| **Shaken** | −1 Evasion, −1 Armor, and a worsened Mettle. The whole card degrades uniformly. |
| **Frozen** | Shaken's penalties, **and no Move actions.** Can still Shoot and Fight. |
| **Routing** | Must spend its entire activation moving toward the nearest board edge. Reaching it removes the unit from play. |

**Vehicles** run the same four steps but end in **Destroyed** rather than Routing.

**Courage** re-rolls failed Mettle checks. **Fearless** ignores suppression markers on Mettle checks — the two are deliberately separate, reusable pieces rather than one bundled trait.

## 6. Cover & Terrain — Composable Tags

Terrain is a set of tags; any piece can carry any combination. The fictional name is flavor.

| Tag | Effect |
|---|---|
| **Obscuring** | +1 Evasion against attacks targeting units benefiting from it. |
| **Cover** | +1 Armor. |
| **Difficult** | Costs double movement. |
| **Blocking** | Fully blocks line of sight through it. |
| **Dangerous** | Each model entering or moving through rolls d10; **4+ passes.** Each failure inflicts 1 wound. |
| **Impassable** | No unit may move through it, full stop — a solid obstruction (a mountain, a building) that `Flying` and Grav Engines don't help with either. |
| **Void** | Ground-based movement cannot cross it at all. Units with `Flying` or the Grav Engines locomotion upgrade cross freely — a chasm or open water has no surface to drive on, but nothing stopping something that isn't touching the ground. |

A ruin is `Obscuring + Cover + Difficult + Blocking`. A sandbag line is `Obscuring + Cover`. A minefield is `Dangerous`. A chasm or river is `Void`; a mountain or a building's footprint is `Impassable`.

**`Impassable` used to read "ground units cannot move through," which already implicitly let Flying units cross — that behavior is now split explicitly into two tags instead of one ambiguous one.** Introduced alongside Oathkeepers' Grav Engines locomotion upgrade, which needed a real distinction between "no surface to drive on" and "solid rock in the way" to make hovering over difficult terrain mean something coherent.

Blast, Engulf, and template weapons ignore cover entirely — their targets cannot benefit from it.

**True line of sight** throughout — base size implies a volume.

## 7. The Two Axes — TYPE and CATEGORY

Every unit carries two labels, and **both carry rules.**

- **TYPE** — what the unit *is*. Six: **Infantry, Cavalry, Vehicle, Monster, Aerial, Towable**.
- **CATEGORY** — its battlefield role, and the Platoon slot it fills. Six: **ARMOR, COMMAND, LINE, RECON, SHOCK, SUPPORT**.

In the data every unit takes one CATEGORY as primary and one TYPE as secondary — e.g. the APC is `Support` (primary) + `Vehicle`; the AFV is `Armor` + `Vehicle`; the Regimental Officer is `Command` + `Infantry`.

### CATEGORY rules

| Category | Grants |
|---|---|
| **ARMOR** | **Bulwark** — reduce all incoming damage by 1, to a minimum of 1. <br> **Hardpoints** — ignore the Heavy weapon trait. |
| **COMMAND** | **Leadership Aura** — units within 12" may use this model's Mettle instead of their own. |
| **LINE** | **Boots on the Ground** — does not need to spend an action to claim an objective. |
| **RECON** | **Spotter** — satisfies the requirement for Indirect and Guided weapons; ignores smoke. <br> **Camouflaged** — +1 Evasion while in cover. <br> **All-Terrain** — ignores difficult terrain penalties. |
| **SHOCK** | **Brutal Assault** — reroll hit results of 1 when fighting, or shooting within half range. |
| **SUPPORT** | **Where We're Needed** — every 2" travelled costs only 1" of Speed while within its own deployment zone. |

### TYPE rules

| Type | Grants |
|---|---|
| **Infantry** | **Entrenched** — while in cover, +1 Armor *and* gains `Courage`. |
| **Cavalry** | **Run Them Through** — this unit's weapons gain +1 AP and Suppressing while charging. <br> **All-Terrain** |
| **Vehicle** | **Armored Front** — uses 90° facings. Attacks against the front are made at −1 AP; against the rear, +1 AP. <br> **Hardpoints** |
| **Monster** | **Terrifying** — units that end their activation engaged with this one are forced to make a Mettle check. |
| **Aerial** | **Flying** — ignores models and terrain while moving. <br> **Soaring Above** — on activation, immediately move half Speed, then continue normally. May move off the table edge; if it does, remove it and redeploy it in the same state in the owner's deployment zone. Can only be charged by units with Flying. |
| **Towable** | **Trailor** — may spend an action to hitch to a friendly Vehicle within 3", and an action to unhitch. <br> **Emplaced Weapon** — must spend an action to deploy before making ranged attacks; immobile while emplaced. |

`Flying` is written as its own standalone entry (see glossary) rather than an Aerial-exclusive bundle item — Aerial TYPE grants it alongside `Soaring Above`, but anything can be granted `Flying` on its own (see `Jump Jets`). `Soaring Above` is what actually distinguishes a true aircraft from anything else that merely ignores terrain.

> **Note, superseding the old one below:** `Impact(X)` is **back**, in a genuinely new shape — not a restoration of whatever the original v0.3 draft meant by it. See the trait glossary's `Impact (X)` and `Crushing Impact (X)` entries. `Fear` is still gone; the Monster signature stays `Terrifying`. Cavalry's baseline charge bonus stays `Run Them Through` — `Impact (X)` is a separate, optional trait some Cavalry (and Infantry, and vehicles/monsters via `Crushing Impact`) carry on top of it, not a TYPE-wide replacement.

## 8. List Building — Platoons

Platoon slots are defined directly by CATEGORY. The data currently defines a **Vanguard Formation** force entry that accepts all categories with **no min/max constraints set** — slot limits are not yet encoded.

**Proposed base spread** (not yet in the data):

| Category | Min/Max |
|---|---|
| COMMAND | 1 |
| LINE | 2–4 |
| RECON | 0–2 |
| SHOCK | 0–2 |
| ARMOR | 0–2 |
| SUPPORT | 0–2 |

Named Platoons shift the spread toward an anchor category in exchange for a once-per-game **Platoon Ability** lasting the rest of that round. Proposed: anchor expands to 2–4, LINE drops to 1–3, everything else caps at 1.

- **Line Formation** (LINE) — *Hold Fast:* for the rest of the round, suppression markers do not worsen Mettle checks for units in this Platoon.
- **Spearhead** (SHOCK) — *Break the Line:* for the rest of the round, units in this Platoon resolve Run Them Through at +2 AP instead of +1.
- **Outrider** (RECON) — *Fast as the Wind:* for the rest of the round, units in this Platoon each gain one free Move action.
- **ARMOR Platoon** — *ability undesigned.*
- **SUPPORT Platoon** — *ability undesigned.*

### Embedded units

The data implements embedding directly. A **Rifle Squad** may take:

- **Embedded Leader** — one Regimental Officer (or any COMMAND-category leader unit), which then counts as LINE rather than COMMAND.
- **Embedded Heavy Weapon Team** — one Heavy Weapons Team, which is stripped of SUPPORT and re-categorized as LINE.

Embedding therefore **changes the host's CATEGORY** to match the squad, so an embedded model doesn't consume its own slot.

### Army scaling

1 Platoon per 500 points, minimum 1 Platoon per 1000 points. Activation count is simply unit count; Pass Tokens handle asymmetry.

**No resource economy.** Confirmed — Marcher's Supply/Intel stays in Marcher.

## 9. Missions & Combined Arms

Objective-based scenarios, varied deployment styles. Alternating activation; the round ends when every unit has activated.

**Combined arms is a primary design goal, not a theme.** CATEGORY caps shape what a list *contains*; the three rules below make a mono-arm list *lose*, which is the part that actually matters.

### 1. Objectives need boots

| TYPE | Objectives |
|---|---|
| **Infantry, Cavalry, Towable** | May **claim**. Costs an action — except LINE units, which claim for free (*Boots on the Ground*). |
| **Vehicle, Monster, Aerial** | May **contest** only. They deny an objective to the enemy but can never score it. |

A tank can park on a marker and stop you scoring it forever; it can never score it itself. **Every army therefore needs infantry regardless of doctrine** — the cleanest lever the game has for mandating combined arms, and it costs no new subsystem.

### 2. Terrain density is a rule, not a suggestion

A standard 4'×4' board carries **at least 8 terrain pieces**, of which:

- **3 or more** carry `Difficult`, `Impassable`, or `Void` — ground armor cannot cross freely
- **4 or more** carry `Blocking` — firing lanes are earned, not given

A board failing this is not a legal board. Sparse terrain silently converts the game into a shooting contest, which is the failure mode that kills combined arms.

### 3. Anti-armor must actually kill armor

Dedicated anti-armor weapons need `Damage ≥ 6` against Toughness 10 chassis. Massed armor should be a **trap**, punished by a comparatively cheap specialist. `Anti-[Keyword]` doubling hits supplies the machinery; the stat lines have to honour it.

### The intended shape

Each arm needs a job the others cannot do:

- **Infantry** takes and holds ground. Only it scores.
- **Armor** breaks through and denies, but cannot hold.
- **Artillery** kills at range, is blind without RECON, and is helpless up close.
- **Recon** sees for the artillery and cannot fight.
- **Aerial** strikes anywhere and holds nothing.

Dependencies, not merely roles. Artillery genuinely does not function without a Spotter, and that coupling is the model for everything else.

## 10. Transports

**Transport(X)** where X is a **model** capacity, not a unit count. Defined values in the data: `Transport (6)`, `(11)`, `(14)`, `(28)`. The APC is `Transport (14)`.

**Eligible cargo:** Infantry and Cavalry.

### Dedicated Transports

A Transport may be taken as a **Dedicated Transport** attached to one specific eligible unit during list building. A Dedicated Transport:

- **Takes the CATEGORY of the unit it carries.** A transport carrying a LINE squad *is* a LINE unit, for every rules purpose — `Anti-[Keyword]`, Platoon abilities, doctrine effects, all of it.
- **Does not consume an additional slot** beyond its payload's.
- Must **deploy carrying that unit**, and may never carry a different one.
- Still counts as its own unit for activation and Pass Token purposes.

*(Slot treatment carried over from Marcher, which allots transports "1 per Transport-Eligible Unit" rather than making them compete with combat choices.)*

Transports competing for CATEGORY slots quietly kills combined arms. Under tight caps — Oathkeepers hold SUPPORT 0–1 — buying a transport spends the slot that would have held fire support, so the rational choice is always to walk. This makes mobility a **points** decision rather than a slot decision, which is the one that should govern it.

**Inheriting the payload's category is what keeps that honest.** A slot-free transport with no category would be a free unit with no downside; instead it is a fully exposed member of the formation it serves. Choosing what a vehicle carries chooses what it is vulnerable to — an Oathkeeper gunboat full of LINE infantry is hunted by `Anti-Line`, while a pure tank in the ARMOR slot is hunted by `Anti-Armor`. Two genuinely different threat profiles, chosen at list building.

### Hull classes — capacity versus armament

Capacity and firepower compete for the same hull. This tradeoff is the main design space for vehicles, and it is where a faction's armor doctrine lives.

| Class | Capacity | Armament | Role |
|---|---|---|---|
| **Bus** | 12–14 | Token — one light weapon | Moves mass cheaply. Delivers and leaves. |
| **Gunboat** | 6–8 | Real — a main gun plus secondaries | Fights *and* carries. Fewer bodies moved, but it stays and contributes. |
| **Assault Transport** | 5–6 | Heavy, short-ranged | Expensive. Exists to survive the approach and disgorge into melee. |

**The gunboat is the important one.** A faction whose transports fight does not need many pure tanks — its armor doctrine arrives in the transport slot instead of the ARMOR slot. That is how a faction capped at ARMOR 0–1 still fields serious vehicle firepower, and it couples the arms physically: their tanks are carrying their infantry, so armor and infantry advance together or not at all.

The tension stays honest because a gunboat is priced as a tank *plus* capacity, and because committing it to one squad for the whole game is a real constraint — it goes where that squad goes.

**Embarking / disembarking:** part of a Move action; spend half the unit's Speed (round up). Disembarking places the leader in base contact with the Transport, then resolves remaining movement normally.

**While embarked:** the unit is on the battlefield but doesn't count toward objective control; all measurement is taken from the Transport.

**Open-topped** cargo may still act (measuring from the Transport) but is independently targetable using its own Evasion and Armor, and counts as in Cover. **Closed-topped** cargo cannot act or be targeted.

**Bailout:** when a Transport is removed from play, every embarked model takes a Mettle check; each failure inflicts 1 wound. Survivors are placed within 3" of the wreck. If the Transport was Aerial and the cargo isn't, the cargo is destroyed outright.

## 11. Points

> The values in the NewRecruit data are **placeholders** from learning the platform and are not authoritative. The formula below is the reference; a calculator implementing it lives at `points.py`.

**Target scale:** a standard game is **1000 points / 2 Platoons**, roughly 8–14 units a side, so the average unit lands near **90 points**.

Model cost and weapon cost are computed **separately** and summed, because Evasion is a property of the target rather than of the attacker or its weapon — the two halves genuinely don't interact.

CATEGORY and TYPE rule bundles are **not priced**. Every unit carries exactly one of each, so their value is absorbed into the baseline.

### Step 1 — Model cost

```
Model Cost = 5.83 × Toughness × E × A × S × M
```

| Evasion | **E** | | Armor | **A** |
|---|---|---|---|---|
| 3 | 0.63 | | 3 | 0.89 |
| 4 | 0.71 | | 4 | **1.00** |
| 5 | 0.83 | | 5 | 1.14 |
| 6 | **1.00** | | 6 | 1.33 |
| 7 | 1.25 | | 7 | 1.60 |
| 8 | 1.67 | | 8 | 2.00 |
| 9 | 2.50 | | 9 | 2.67 |
| | | | 10 | 4.00 |
| | | | 11+ | 8.00+ |

- **E** is `1 ÷ P(hit)`, normalised so Evasion 6 = 1.00.
- **A** is `1 ÷ P(damage)` against a reference **AP 1** attack, normalised so Armor 4 = 1.00.
- **S** (Speed) = `1 + (Speed − 5) × 0.06`
- **M** (Mettle) = `1 + (Mettle − 4) × 0.06`

Baselines are Evasion 6, Armor 4, Speed 5, Mettle 4 — a plain grunt, who costs **7 points**.

> **Why the terms multiply rather than add.** Being good at *everything* has to cost superlinearly, or elite units are undercosted by construction. Because Toughness, E, A, S, and M all multiply, an Oathkeeper (T2, ARM 7, SPD 7, MET 6) pays not for durability *plus* mobility but for durability *×* mobility — **3.8× a Guardsman per model**, before weapons. Most units simply cannot afford to be fast *and* armored *and* tough, and that is the intended pressure: **for an elite unit, the cost is the downside.** This is also why the formula can afford to be generous with stat divergence between factions.

> Armor 3 and 4 cost the same. That is a real consequence of "an unmodified 1 always fails": against AP 2, both cap out at a 90% damage chance, so the first points of armor genuinely buy nothing. Armor only starts earning its cost at 5+.

> Evasion 10 would score 5.00 — a 10× multiplier off one stat. **Cap Evasion at 9.**

### Step 2 — Weapon cost

Weapons are priced against **two reference targets**, because a single reference badly misprices anti-tank guns:

- **Soft target** — Evasion 6, Armor 4 → `P(hit) 0.5`, `P(dmg) = min(0.9, (7 + AP)/10)`
- **Hard target** — Evasion 5, Armor 8 → `P(hit) 0.6`, `P(dmg) = clamp((3 + AP)/10, 0.1, 0.9)`

```
Soft  = Attacks × 0.5 × P_soft × min(Damage, 2)
Hard  = Attacks × 0.6 × P_hard × Damage
Value = (Soft + Hard) ÷ 2
Weapon Cost = 6.67 × Value × R × (1 + Attacks × AP × 0.03)
```

The final term is the **penetration × volume premium.** A weapon that is both piercing *and* high-volume is the strongest thing on the table, and pricing each term linearly badly undercharges the combination. It is why a Heavy Machine Gun (A4/AP2/D2) is the most expensive infantry weapon in the game.

`min(Damage, 2)` on the soft score is an **overkill cap** — a Damage 10 shell is no better than a Damage 2 one against a Toughness 1 rifleman, and without the cap every anti-tank weapon prices as though it were also the best anti-infantry weapon in the game.

**Range multiplier R** = `0.6 + Range ÷ 30`, with melee at **0.85**.

| Range | R | | Range | R |
|---|---|---|---|---|
| Melee | 0.85 | | 24" | 1.40 |
| 6" | 0.80 | | 30" | 1.60 |
| 12" | 1.00 | | 36" | 1.80 |
| 18" | 1.20 | | | |

### Step 3 — Weapon traits

Every trait is multiplicative — a trait's value scales with how much the weapon already does, so its cost should too. A flat add taxes a cheap weapon heavily and an expensive one barely at all, which is backwards.

Rather than individually arguing ~15 trait values — exactly the kind of subjective, hard-to-defend pricing this system otherwise avoids — traits are grouped into **two bonus tiers and two restriction tiers**, each one fixed multiplier. Retuning the whole system is changing four numbers, not fifteen.

**Bonus tier** — does the trait change the *shape* of the attack (major), or just improve the odds on an otherwise-normal shot (minor)?
**Restriction tier** — does it narrow *what* can be targeted (minor), or *when* the unit can act at all, or *how completely*, (major)? `Frontal/Rear/Side Arc` moved to major once `Traversing` existed as a real comparison: a **permanently** fixed arc never reaches the rest of the board, while `Traversing` eventually reaches all of it, just slowly — pricing them the same was only ever an artifact of Arc being the sole data point.

| Tier | × | Traits |
|---|---|---|
| Major bonus | **1.30** | Linked-Weapon, Blast (L), Engulf (L), Guided, Indirect, Overcharge, Precision |
| Minor bonus | **1.10** | Accurate, Blast (S), Engulf (S), Suppressing, Turret, Pistol |
| Minor restriction | **0.90** | Coaxial, Traversing |
| Major restriction | **0.75** | Heavy, Frontal / Rear / Side Arc |
| Anti-[Keyword] *(each, stacks)* | **1.20** | — |

**Multiple traits compound, they do not add.** A weapon with traits `A` and `B` costs `base × A × B`, not `base × (1 + (A−1) + (B−1))`. This is a deliberate choice, made explicit here because it isn't the only reasonable one and the two diverge fast: two Major bonuses stacked is a 5.6% gap between compounding and adding; three is 15.6%; a hypothetical five-trait weapon is 48.5%. At the trait counts currently on the roster (2–3), the two are nearly identical — the gap only bites on a weapon someone loads up with everything.

Compounding is *derived*, not merely chosen, for the model-stat formula above — `Toughness ÷ (P_hit × P_dmg)` is a real multiplicative relationship, so an elite model being tough *and* evasive *and* fast is genuinely superlinear survivability. Weapon traits have no such derivation; the tier multipliers are hand-picked, same as ever. So this is a free design decision, not a mathematical necessity, and it was made **for consistency with that same instinct**: specialization is already the theme of the weapon tiers (Obliterator, Automatic, and Special are deliberately single-purpose, not swiss-army guns), and compounding actively discourages stacking many bonus traits onto one weapon, which reinforces rather than fights that theme.

### Step 4 — Unit size scaling

Chassis, weapons, and Transport are summed, then multiplied by:

```
Size Factor = (N ÷ 10) ^ −0.15          [unit cost scales as N^0.85]
```

| Models | Factor | | Models | Factor |
|---|---|---|---|---|
| 1 | 1.41 | | 8 | 1.03 |
| 2 | 1.27 | | 10 | **1.00** |
| 3 | 1.20 | | 16 | 0.93 |
| 5 | 1.11 | | 20 | 0.90 |

**Why:** in alternating activation the scarce resource is the **activation, not the model**. Sixteen bodies delivering one activation are worth less per model than five delivering one. Overkill waste and coherency drag push the same direction.

Note that *degradation* is **not** the justification, despite being the intuitive one. Average output over a unit's lifetime is `(N+1)/2N`, which collapses immediately and then flattens — 55% at 10 models, 53% at 16. It cannot explain a discount between those two sizes.

Hand-priced extras sit **outside** this curve.

### Step 5 — Special/named unit abilities: flat, not multiplicative

Priority Orders, Leadership Abilities, Triggered effects (Blood Surge and anything shaped like it). These get **flat point costs**, on principle — a weapon trait multiplies because it modifies a base the weapon already has (its own Attacks/AP/Damage output), and a stat multiplies because durability is a genuinely multiplicative relationship. A standalone ability like *"ignore Shaken entirely"* or *"reroll any die once per game"* doesn't modify either kind of base — it's a capability, not a modifier — and its value has essentially nothing to do with how many guns the unit happens to be carrying. Charging a percentage of the unit's grand total would make the same ability cost more on a unit that spent its points on weapons and less on one that spent them on chassis, which has nothing to do with what the ability actually does.

Same two-tier logic as the weapon traits, just flat instead of a multiplier:

| Tier | Cost | Use for |
|---|---|---|
| **Major** | **15** | Meaningfully changes how the unit survives or plays — ignoring a whole state (Shaken, Suppressing), a strong once-per-game reroll, a wide-reaching aura |
| **Minor** | **5** | A narrow or conditional edge — situational, small in scope, or rarely relevant |

The 3× ratio matches the bonus-trait tier gap (1.10 vs 1.30). These sit **outside the size-scaling curve** — they usually attach to one model (a leader's Priority Order), not the whole squad, so they shouldn't get cheaper because the squad is large.

### Other surcharges

- **Transport(X)** — `X × 0.417` points.

### The currency scale

`BASE_MODEL` and `BASE_WEAPON` move **together**. Multiplying both by the same factor rescales every cost in the game proportionally and changes no relative balance whatsoever — it is a pure unit conversion. They are calibrated so the anchor unit, a 10-model Rifle Squad with rifles and bayonets, lands on exactly **100 points**.

A 1000-point list is therefore *ten rifle squads' worth of stuff*, which is the intended mental model.

### Validation — Imperial Regiments

| Unit | Models | Total | Per model |
|---|---|---|---|
| Conscript Mob | 16 | 80 | 5.0 |
| **Rifle Squad** | 10 | **100** | 10.0 |
| Veteran Squad | 8 | 112 | 14.0 |
| Storm Squad | 8 | 141 | 17.6 |
| Scout Element | 5 | 67 | 13.4 |
| Regimental Officer | 1 | 58 | — |
| Heavy Weapons Team | 1 | 78 | — |
| Field Gun Battery | 1 | 57 | — |
| Armored Personnel Carrier | 1 | 117 | — |
| Tank Destroyer | 1 | 176 | — |
| Armored Fighting Vehicle | 1 | 241 | — |

Chaff → line → veteran reads **5.0 → 10.0 → 14.0** per model. The Conscript Mob fields 16 bodies for less than the anchor's cost, which is exactly what chaff should do.

> **Open:** the AFV at 241 is 2.4 rifle squads — 24% of a 1000-point list. That follows from the single-model premium stacking on an already-expensive chassis. The ratio is in line with comparable games, but if centrepieces feel over-taxed, soften `SIZE_EXPONENT` from 0.85 toward 0.90.
>
> These numbers move whenever the weapon library or a unit's loadout changes — re-run `python build_cat.py factions/imperial_regiments.json` rather than trusting this table blind.

---

## Reference — Stat & Weapon Templates

### Unit Profile

`Speed | Mettle | Evasion | Armor | Toughness`

- **Speed** — inches of movement.
- **Mettle** — morale. Additive, higher-is-better (see §5).
- **Evasion** — attackers roll ≥ this to hit. Higher is better for you.
- **Armor** — attackers roll ≥ this (after AP) to damage. Higher is better for you.
- **Toughness** — the wound pool. Replaces the old "Wounds" stat.

### Weapon Profile

`Range | Attacks | Armor Piercing | Damage | Weapon Traits`

### Weapon & unit trait glossary

**Targeting & templates**
- **Blast (S/L)** — may target a point instead of a model, centring a circular template. On a miss, scatter the point of impact 1d5" (S) or 1d10" (L) in the direction rolled. Targets cannot benefit from cover.
- **Engulf (S/L)** — uses a small or large teardrop template; targets cannot benefit from cover.
- **Indirect** — may target an enemy without line of sight, provided an allied unit with Spotter has line of sight to that target.
- **Guided** — if the target is visible to an allied RECON unit, this weapon's attacks against it need a flat **3+** to hit, replacing the target's actual Evasion entirely and disregarding every other modifier, including range bands. *(Changed from a flat "−3 Evasion" under the d10 engine — a straight replacement avoids the target's real Evasion ever mattering at all, and avoids a subtractive modifier ever making an already-easy shot harder.)*
- **Accurate** — this weapon has no Long Range penalty: Attack Rolls at Long Range are made as though at Effective Range. Keeps the Close Range bonus. *(Earlier wording said "ignore all range modifiers," which would also have stripped the +1 at Close Range.)*
- **Optics** — the target cannot gain Evasion bonuses from being Obscured or in Obscuring terrain. Cuts through concealment rather than boosting raw accuracy — deliberately a different job than `Accurate` (which answers range, not cover). No longer a stub; needs a pricing tier assigned (currently costs nothing in the points formula, which is now wrong). *(First application: Oathwarden Squad's Carbine/Optics configuration.)*
- **Precision** — when resolving this weapon's attacks, its controller may choose which model within the target unit receives each hit, instead of following the unit's normal allocation order. Bypasses the protection a unit's own arrangement would otherwise give a key model — an NCO, a special-weapon carrier, a `Caster`. Priced as a Major bonus: like `Guided`, it changes the shape of what the attack can affect rather than just improving the odds on a normal shot — arguably more so, since it defeats allocation entirely rather than just Evasion. *(First intended application: a Saints sniper/support weapon, not yet named or built.)*

**Firing restrictions**
- **Heavy** — cannot attack in the same activation its unit moved; if it attacks first, it cannot then move.
- **Hardpoints** — ignore the Heavy trait.
- **Bombardment** — this unit ignores the Heavy trait on its weapons. However, if it moved this activation, its ranged attacks made this activation lose Indirect — they must have line of sight to their target, and may not target a model visible only to an allied unit with Spotter. The first trait in the game that makes a unit deviate from the blanket "every Vehicle ignores Heavy via Hardpoints" rule on purpose — a unit with `Bombardment` does not also have `Hardpoints`. Deliberately a qualitative cost rather than a statistical one (an earlier draft considered a flat Evasion penalty for firing after moving): sometimes moving costs nothing, since the target was visible anyway; sometimes it costs the entire shot. *(First application: the Tayra, a self-propelled mortar/gun carriage — a properly sighted-in crew hits what it aims at, a crew that just displaced hasn't caught its breath yet.)*
- **Pistol** — may make a ranged attack while engaged, but only at an enemy unit it is engaged with.
- **Turret** — may fire from any facing.
- **Frontal / Rear / Side Arc** — may only target models in that facing, permanently.
- **Traversing** — this weapon tracks its own facing, starting aligned with the hull's. At the start of this unit's activation, its facing may be rotated up to 90° before firing. It may only target models within its current facing. Unlike a fixed Arc, it eventually reaches anywhere — a target 180° away costs a full activation of pure rotation before the gun can fire on it at all, during which the vehicle is genuinely exposed on that flank. *(First application: the Sable's Light Cannon package — the turret ring can take the gun, but swinging it is slow.)*
- **Coaxial** — must target the same target as the weapon named in the annotation.
- **Linked-Weapon** — reroll all misses.

**Damage & suppression**
- **Suppressing** — targets gain a suppression marker regardless of the attack's outcome.
- **Barrage** — when this weapon hits a unit, that unit must immediately make a Morale test. Not yet transcribed into `PraxisBelli.gst` — referenced on Prophesier MBT's Purification Launcher (`Barrage, Indirect`) but currently undefined there. *(First application: Purification Launcher, Prophesier MBT.)*
- **Overcharge** — this weapon may fire in Overcharged mode: its AP and Damage are each increased by 2 for that attack. For each unmodified roll of 1 made for this weapon's attack, the bearer suffers a Damage 1 hit that cannot be saved against, in addition to any other effect of that roll.
- **Caster** — a standalone keyword, independent of TYPE and CATEGORY, granted to specific models (priests, psykers, sorcerers, and other channel-a-power archetypes) rather than defining a new TYPE or CATEGORY of its own — the same "anything can be granted it" pattern already established for `Flying`. Exists primarily so `Anti-Caster` has something to target; the actual casting/power mechanics a Caster-tagged model might use are undesigned and out of scope for now.
- **Anti-[Keyword]** — against a target with the matching keyword, each successful damage roll counts as two hits instead of one; because hits are allocated individually, the excess may spill onto other models in the unit. Defined for: Aerial, Armor, Caster, Cavalry, Command, Infantry, Line, Monster, Recon, Shock, Support, Towable, Vehicle.
- **Bulwark** — reduce incoming damage by 1, to a minimum of 1.
- **Ablative Plating** — grants `Negates (Anti-Vehicle)` and `Negates (Anti-Armor)`. Narrower than a flat Armor increase on purpose: it specifically answers weapons built to kill vehicles, rather than making the model tougher against everything. Industrial materials science, not warded plate — the sci-fi register stays technological rather than borrowing anything from the Oath, since the faction using it first (Regiments) has no oath-access at all. *(First application: the Sable's standalone Ablative Plating option.)*
- **Warded Plate** *(name provisional)* — grants `Negates (Anti-Infantry)`. The infantry-scale cousin of `Ablative Plating`, and a direct payoff of the line above — Oathkeepers (Deep Oath) are the first faction with the actual oath-access to earn the "warded" version rather than the merely industrial one. *(First application: Oathkeepers' Terminator-tier Heavies, alongside `Shrug`.)*
- **Indomitable** — reduce the AP of incoming attacks by 1, minimum 0. Doesn't stop a dedicated anti-armor weapon from doing its job, but meaningfully blunts anything that wasn't built to punch through this specific armor. Deliberately not named `Bulwark` (already in use, and means Damage reduction, not AP reduction — a real naming collision caught before it shipped). *(First application: Oathkeepers' Heavies/Terminator-equivalent tier.)*
- **Crushing** — this weapon's Damage is increased by 1 against a target with Toughness 5+, and by 2 against a target with Toughness 10+. Deliberately named for what it does, not for any one weapon's fictional flavor, so it can be reused on future weapons that hit harder against heavy targets without being reskins of the same gravity-tech idea. The Toughness 10+ threshold isn't arbitrary — it lines up with the Armor-above-10 cascade threshold, so this trait reads as a direct answer to exactly the kind of target that rule exists for. *(First application: an Oathkeeper NCO sidearm option.)*
- **Shotgun** — this and `Meltdown` are **range-band-conditional**: their effect changes depending on which band the attack was fired from, rather than being a flat always-on modifier like every other trait above. At Close Range, re-roll all failed Attack Rolls. At Long Range, this weapon cannot be fired. Represents a close-range weapon that's devastatingly reliable up close and rapidly falls off past that — a hard cliff rather than a gentle taper. *(Rewritten for the Close/Effective/Long bands. The earlier "+2 Evasion at the outer band" penalty was a ±2 modifier, which the modifier policy now forbids; "cannot fire at Long Range" is the floor-style replacement and is a proposal — if the cliff should be softer, the alternative is a flat 5+ Attack Roll at Long Range.)* *(First application: the generic Scattergun weapon, D2; the Oathkeeper-exclusive `Oathkeeper Scattergun` variant runs D3.)*
- **Meltdown** — at Close Range, re-roll all failed Attack Rolls. If fired at Effective or Long Range instead, re-roll all **successful** Attack Rolls — a harsher penalty than Shotgun's, appropriate since Fusion-pattern weapons already sit in anti-armor territory and need a stronger reason not to just be fired from a safe distance. Applies to **every Fusion-pattern weapon in the roster retroactively** (Fusion Blaster, Heavy Fusion Blaster, and any future Fusion Pistol), not just new ones — the name is a deliberate near-homophone for Melta, the real-world-adjacent tech Fusion weapons are meant to evoke in this setting's fiction, the same naming trick as `HAMR`/hammer.
- **Impact (X)** — on a successful charge, roll X dice **per charging model** against the target unit's Armor, AP0, Damage 1 each. **Not an attack and doesn't use any weapon** — it resolves in total isolation, unaffected by weapon traits, Anti-[Keyword], or anything else that modifies an attack, because it represents the sheer physical weight of the charge and nothing else about the unit. Most effective against light/unarmored targets by design (AP0 means it never threatens real armor, only bulk-and-numbers). A genuine revival of the cut v0.3 `Impact(X)`, but a new shape, not a restoration — the old version is not what this is. Guideline rather than a hard TYPE lock: Infantry and Cavalry are the register this belongs to. X is driven by the individual model's own weight/violence of impact, not the unit's size — a jump-pack trooper might carry Impact (1), while something dropping from orbital height carries Impact (3), regardless of squad size either way.
- **Crushing Impact (X)** — the Vehicle/Monster register of `Impact (X)`, same structure and same isolation from weapons/traits. Currently stubbed at AP3/Damage 2 pending a real application — enough to threaten light armor or anything under Toughness 3, not enough to meaningfully touch another vehicle. *(First real application: Bastion — whether Vehicles get a standard melee profile at all, the way Infantry has universal Fists, or whether some vehicles rely on Crushing Impact alone with no ongoing melee option, is a genuinely open question, not yet decided either way.)*
- **Consumable (X)** — this weapon may only be used X times over the course of the game; once its uses are exhausted, it cannot fire again. Parallel notation to `Anti-[Keyword]`, `Deployment (X)`, and `Impact (X)` — a general-purpose way to describe limited-ammunition or one-shot weapons rather than inventing a bespoke rule per weapon. *(First application: Bastion's Hunter-Killer Missile, `Consumable (1)`.)*
- **Lance** — +1 AP on charge. The first trait priced under the new flat points formula: a flat +0.5, regardless of the weapon it's on. *(First application: the Heavy Ripsaw Sword, Repentia Squad — paired with `Onslaught` below, so charging turns a plain AP1 blade into effective AP2 with rerolled hits; off the charge it's just AP1.)*
- **Onslaught** — while charging, reroll failed hit rolls made with this weapon. A one-time reroll, not chainable against a second failure. Deliberately framed as the physics of impact (a charging body knocking the target's guard down for an instant) rather than personal fury, which keeps it distinct from the established "zealotry/fervor rerolls damage, not hits" convention (`Martyrs, all`, `Wrathbound`) — that rule is about anger sinking the blow deeper, this is about the shock of the charge itself, a different axis entirely. *(First application: the Heavy Ripsaw Sword, Repentia Squad.)*
- **Extra Hits (X)** — when this weapon's hit roll is X or higher, it generates one additional hit, resolved normally (including its own separate damage check). Defaults to X = 10 (a true Critical Hit) unless the weapon's own profile states a lower threshold — that threshold is the actual design lever, since a weapon at `Extra Hits (7)` fishes for the bonus constantly while one stuck at `Extra Hits (10)` only spikes on the rare hot streak. *(First application: the Heavy Ripsaw Sword, Repentia Squad, at `Extra Hits (10)` — deliberately kept at the stingy default so it reads as a spike, not a new baseline: normally an above-average blade, a genuine nightmare unit when the dice run hot.)*
- **Critical (X)** — when this weapon's hit roll is X or higher, that hit automatically succeeds its damage check without rolling. Same threshold convention as `Extra Hits (X)`. Deliberately scoped to specific weapons rather than the universal Critical Hit rule itself — see the note under "Critical Hit" above for why a blanket version of this would be a real problem, not just a strong one.
- **Negates (X)** — this model treats attacks or effects carrying [X] as though they did not carry it; everything else about the attack or effect still resolves normally. A general "hard immunity to one specific named thing" family — the defensive mirror of `Anti-[Keyword]`'s "specifically punishes one named thing." Retroactively absorbs two existing traits that were always this shape under a bespoke name: `Ablative Plating` and `Warded Plate` (see below), both of which keep their flavor names and fictional grounding but are now defined as grants of this shared primitive rather than one-off rules text. *(First new application: Repentia Squad's `Negates (Suppressing)` — they don't gain suppression markers from Suppressing weapons at all, the mechanical expression of a unit that's already stopped caring whether it dies.)*

**Cost-modifying traits**
- **Conscript** — this unit costs **25% less**. It may never re-roll a die for any reason, and may not take the Rally action. *Conscripts get raw numbers and none of the benefits of training: `Entrenched`'s Mettle re-roll and `Massed Ranks`' to-hit re-roll both go dead, and once suppressed they can only clear markers one at a time by passing checks they are bad at.*
- **Mindless** — this unit costs **10% less** *(proposed, flagged for playtesting — the bundle below is genuinely mixed, not purely a downside like `Conscript`, so it's priced far lighter)*. This unit automatically passes Morale tests and cannot benefit from cover. If an enemy unit is within charge distance at the start of this unit's activation, it must declare a charge against the nearest such enemy unit. Built for units with no will of their own to break — a real reusable primitive, not bespoke to whichever unit debuts it: immune to the game's entire morale-track failure mode, at the cost of a defensive tool (cover) and all positioning agency once an enemy is close enough to reach. *(First application: Arco-Flagellants.)*
- **Critical Weakspot** — a discount, not a weapon surcharge, since it modifies what the *model* costs rather than what a weapon does. When a Damage check against this model is rolled as an unmodified 10, the attacking weapon's Damage is doubled instead of applied normally. A rare, high-drama vulnerability rather than a steady tax — priced like `Conscript`, as a modifier on the unit total, not folded into the weapon-trait tiers. *(First application: the Marten's extended-fuel-tank package — exposed fuel is a real historical liability, not just flavor text.)*
- **Fixed** — this weapon cannot be removed, swapped, or exchanged for an upgrade. Used for equipment that comes as part of another weapon, such as a Bayonet on a Rifle.

**Medical support**
- **Combat Medic** — two linked effects on the same unit, one passive and one action-based:
  - *Passive:* while a friendly Infantry or Cavalry unit is within 6" of this model, a model in that unit that would be removed as a casualty instead makes a Mettle check. On a pass, it is not removed and is instead treated as having 1 wound remaining.
  - *Active:* as an action, this model may restore 1d5 lost wounds to models in one friendly Infantry or Cavalry unit within 6" — the same recovery rate `Regeneration` already uses, delivered externally rather than by the model's own biology.
  - Deliberately scoped to Infantry/Cavalry only. A Mettle check makes sense for something with a will to keep fighting to check against; a vehicle's failure modes don't work that way. Vehicle repair is a different mechanic for a different unit, not yet designed.

**Durability & morale**
- **Regeneration** — at the end of every round, regain 1d5 lost wounds.
- **Courage** — re-roll failed Mettle checks. *(Split out from the old Fearless, which used to bundle this with ignoring suppression markers — the two are more useful as separate, independently reusable pieces than as one combined trait.)*
- **Fearless** — ignores suppression markers on Mettle checks (the check is made as if the unit held none). No longer bundles Courage's re-roll — see above.
- **Entrenched** — while in cover, +1 Armor and gains `Courage`.
- **Camouflaged** — +1 Evasion while in cover.
- **All-Terrain** — ignores difficult terrain penalties.
- **Shrug (X)** — for every wound this model would suffer, roll a d10 and ignore that wound on an X or better (the universal floor/ceiling applies: an unmodified 1 always fails, an unmodified 10 always succeeds). The system's version of an invulnerable save — deliberately rare by design intent, reserved for specific named wargear rather than a unit-wide rule, so it stays a genuine event rather than a roll made on every single hit across the whole army. *(First intended application: a Storm Shield-equivalent Oathkeeper wargear option, possibly also an Iron Halo-equivalent for Oathmaster — neither built yet.)*
- **Undaunted (X)** — when this unit fails a Mettle check that would step it down its morale track, it may immediately attempt one additional, unmodified roll against a fixed target number of X; on success, it does not step down. Mechanically `Shrug`'s own shape — a flat second roll against a static threshold, not modified by the model's own stats — retargeted at morale instead of damage. Kept as its own name rather than overloading `Shrug`, since two different effects can't share one trait name (the same rule that separated `Bulwark` from `Indomitable`). *(First application: Repentia Squad, at `Undaunted (7+)`, gated on a Repentia Superior being present in the unit — kill her, and it stops working for whoever's left.)*

**Movement**
- **Flying** — ignores models and terrain while moving. Now a standalone entry rather than an Aerial-TYPE exclusive: anything can be granted it. Aerial TYPE grants it alongside `Soaring Above`, which is what actually distinguishes a real aircraft from anything else that merely ignores terrain.
- **Jump Jets** — grants `Flying`, and grants `Impact (X)` on a successful charge. *(First application: Inceptors baseline; a Tacticus-pattern Assault Squad as an optional upgrade, at a lower X than Inceptors carry by default.)*

**Deployment (X)**

A notation family for special deployment-phase rules, parallel to `Anti-[Keyword]` and `Blast (S/L)` — the bracket names *which* deployment method, and each variant resolves in a fixed order during the deployment phase itself, before the first activation of the game. Renamed from the original standalone `Scout Move` once a second variant (`Infiltrate`) needed a shared naming convention.

- **Deployment (Scout)** — after normal deployment, this unit may make a free move up to its Speed. Resolves first, before any other Deployment(X) variant. *(First application: the Weasel.)*
- **Deployment (Infiltrate)** — this unit does not deploy in the normal sequence. After every `Deployment (Scout)` move has resolved, place this unit anywhere on the battlefield more than 9" from any enemy model. Resolves after Scout on purpose — an Infiltrate unit gets to see where the board actually ends up before committing to a spot, unlike a traditional mid-game deep strike, this never waits for a later turn; it's a later *step* of the same deployment phase, not a separate arrival mechanic. *(First application: Oathreapers. Distance shape-proposed, not locked.)*

**Reserved, not yet spent:** `Deployment (Airborne)`, `Deployment (Burrowing)` — distinct fictional arrival flavors, mechanisms not yet designed. `Deployment (Targeted)` is reserved as the deliberate catch-all for any teleportation-style arrival — one shared mechanic for "appears at a chosen point," regardless of which faction's fiction (warp, teleporter, etc.) explains it, rather than a new bracket variant per flavor.

- **Picket** — once this unit has deployed, enemy units cannot be deployed or redeployed within 8" of it — covers both normal deployment and any `Deployment (X)` arrival. The system's first defensive answer to the Deployment (X) family itself, not just another way to arrive. *(First application: Oathwarden Squad. `Ward` was considered and set aside — kept in reserve for a future rule interesting enough to earn it.)*

---

## Roster — Imperial Regiments

**The canonical roster lives in `factions/imperial_regiments.json`** (source) and `reference.html` §13 (formatted, with full stat cards and the weapon library table) — not here. Duplicating full stat blocks in a third place is exactly the kind of drift this note exists to prevent: an earlier version of this section listed units and weapons (Infantry Commander, Fusion Blaster, Ripsaw Sword) that no longer exist anywhere else in the project. Regenerate the `.cat` from the JSON with `python build_cat.py factions/imperial_regiments.json`.

Current roster, for orientation: **Levy** (chaff), **Fusilier** (anchor), **Grenadier** (veteran), **Vanguard** (shock), **Ranger** (recon), **Ballistier** (flexible heavy weapons, provisional name), **Officer** (command) are fully built. **Sapper**, **Hunter**, and **Dragoon** have locked identities and (Dragoon's case) a fully-designed signature rule, but no stat lines yet — see `faction-identity.md` and the naming table in `reference.html` §14.

### Weapon tiers

Three tiers by what carries the weapon, not by what it's for — see `reference.html` §13 for the full current library:

- **Tier 1 — Infantry**: man-portable, one operator (Rifle, Carbine, Sidearm, Marksman Rifle, ATGM, etc.)
- **Tier 2 — Crew-served**: a small team, or a vehicle's secondary/hull mount (MGs, Autocannons, Mortar, Missile Launcher/Heavy ATGM)
- **Tier 3 — Vehicular/Towable**: needs a hull or a carriage (Main Cannon, Field Howitzer, MLRS)

---

## Open Threads

Genuinely open as of the last working session — most of the original v0.3 list (Mettle direction, who rolls damage, the AP scale, Transport/Indirect/Smoke rule text, the superseded data folder) has since been resolved and removed from this list.

1. **Trait-tier and ability-tier multipliers are still guesses** — the four weapon-trait tier values, the five faction signature-trait multipliers, and the two ability tiers are all hand-picked. Everything else in the points formula derives from probability. First thing playtesting should attack.
2. **Sapper, Hunter, and Dragoon have no stat lines.** Sapper is additionally missing its actual terrain-clearing rule (`Breach`, conceptually settled, not yet written up formally) — the one piece that answers this document's own §9 terrain-density requirement.
3. **`Optics` now has a real mechanism** (ignores Evasion bonuses from Obscured/Obscuring terrain) but still needs a pricing tier assigned in points.py — currently costs nothing, which is now wrong rather than a placeholder.
4. **ARMOR and SUPPORT generic Platoon Abilities** are undesigned (the five faction-specific doctrines exist; the three generic Vanguard-Platoon abilities from §8 are Line/Shock/Recon only).
5. **Platoon slot constraints aren't encoded in the `.gst`** — the proposed spread in §8 is documented but not enforced by the force entry itself.
6. **The AFV's cost is 2.4 rifle squads.** If centrepieces feel over-taxed, soften `SIZE_EXPONENT` from 0.85 toward 0.90 in `points.py`.
7. **No mission or scenario** has been written against the current rules.
8. **No general facing/LOS section** — `Armored Front` and the arc traits imply one exists, but it isn't written.
9. **The toolchain is duplicated** across the `Praxis Belli` project workspace and the `PraxisBelli` git repo (copied, not moved) — a real drift risk until one is picked as canonical.
10. **`PraxisBelli.gst` is missing roughly 30 rules that already exist in this glossary and in faction-identity.md.** The user is keeping the `.gst` as-is and rebuilding the three `.cat` rosters from scratch by hand rather than resetting everything — this list is what still needs transcribing into the `.gst` at some point during that rebuild (definitions live at their linked source, not repeated here, to avoid a third copy going stale):
    - **Weapon/unit traits** (full text in this document's glossary, §"Weapon & unit trait glossary" above): `Bombardment`, `Traversing`, `Ablative Plating`, `Indomitable`, `Crushing`, `Shotgun`, `Meltdown`, `Impact (X)`, `Crushing Impact (X)`, `Consumable (X)`, `Conscript`, `Critical Weakspot`, `Fixed`, `Combat Medic`, `Courage`, `Shrug (X)`, `Jump Jets`, `Deployment (Scout)`, `Deployment (Infiltrate)`, `Picket`, `Barrage`.
    - **Faction signature traits** (full text in faction-identity.md, per-faction "Signature trait —" entries): `Massed Ranks` (Regiments), `Bound Spirit` (Forgesworn), `Oathbound` (Oathkeepers), `Martyrs, all` (Saints), `Wrathbound` (Wrathful Oathbreakers).
    - **Platoon Doctrines** (faction-identity.md, per-faction "Doctrine —" entries): `Fix Bayonets`, `Sealed Orders`, `Hold the Oath`, `Act of Faith`, `Break the Chains`.
    - **One not-yet-in-glossary trait**: `Warded Plate` (faction-identity.md, Oathkeepers' Heavies/Terminator family section) — name still provisional.
    - **Present in the `.gst` but with stale text needing a rewrite, not an addition**: `Fearless` (likely still the old bundled version), `Entrenched` (likely still says "reroll failed Mettle checks" instead of granting `Courage`), `Optics` (likely still the old priced-at-0 stub text).
11. **The v0.5 redesign is in progress.** §3 and the §5 Mettle-check formula are converted to d6; everything else — the Role/Keyword collapse, morale redesign, Formation/CORE, the full points-formula rebuild, the `Fists`→`CCW` rename — is specified in the **v0.5 Decision Queue** near the top of this document and not yet applied to the sections below. Every faction/unit stat line in `factions/imperial_regiments.json` was built against the d10 curve and is stale until the formula is rebuilt. Two gaps surfaced during the dice conversion need real design work, not just arithmetic: an **AP overkill cap** (§3, "Armor's floor") and a **Mettle value recalibration** for d6.
