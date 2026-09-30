# Praxis Belli — Design Bible

**Status:** v0.5-in-progress — converting the core dice engine from d10 to d6 for component accessibility (most players own dozens of d6, far fewer own enough d10 to roll a whole squad's attacks at once). This is a breaking change to the probability foundation everything else is built on, being carried out one section at a time; sections not yet touched still describe the d10-era numbers and are marked as such. `reference.html` (the formatted twin) has **not** been updated yet and will drift out of sync until a dedicated pass syncs it — treat this document as authoritative during the conversion.

**Source of truth — two modes, not one:** while actively building or revising stats and profiles together, this document and `points.py`/`factions/*.json` lead — that's what a design session *is*. Outside of that, **NewRecruit is the default source of truth**: `PraxisBelli.gst` and the `.cat` files in `C:\Users\darry\Documents\NewRecruit\data\PraxisBelli\` reflect whatever was last hand-edited there directly, which may not match what's written here. When the two disagree, that's a conflict to surface and resolve, not something to silently overwrite in either direction. The older `Documents\NewRecruit\data\Praxis Belli\` folder (with a space) is superseded regardless of either mode; it holds an earlier `Praxis Belli.gst` plus Oathbreaker Legions / Oathkeeper Cohorts catalogues on a different game system ID.

**Design lineage:** *Marcher: EAW* (Platoon frame, Transports, attacker-rolled Evasion/Armor), *Ravaged Star* (d10 roll-over engine, 1-fails/10-succeeds, the Damage stat, "Shaken"), and *Warmachine MkIV* (facings and arcs, model-count transports).

### v0.5 Decision Queue — decided, not yet written into the sections below

Snapshot of the latest design decisions as of 2026-09-28. **Already applied in this document:** the d6 conversion (§3, §5's Mettle-check formula, `Guided`, range bands), **item 1 (Role/Keywords — §7, with knock-on fixes through §1/§8/§9/§10/the glossary)**, **item 2 (Morale redesign — §5, now 2d6, plus a new Damage Track mechanic for single-model units)**, **item 3 (Platoons/CORE — §8)**, and, as of a from-scratch rebuild later the same day, **item 4's core formula (§11 — Model Cost, Weapon Cost, `Anti-[Keyword]` pricing, weapon-trait and named-ability tiers, `Transport(X)`, and the new Size stat)**. **Still genuinely not applied:** §4's own `Fists`→`CCW` section rewrite (the decision — CCW is 0 points — is made, just not yet written into that section's prose), exhaustive classification of every remaining trait against the new tiers, the four faction signature-trait multipliers, actually re-costing the roster against the new formula, and item 6 (the smaller d10-notation cleanup listed below). Where this list and an older section below disagree on any of those, this list still wins. Legacy snapshots of every doc as they stood before this work are saved alongside as `*_legacy.*`.

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
3. **Platoons / CORE** (rewrites §8's Named Platoons). Choosing a Platoon designates a **CORE** Role/Keyword. *Only* CORE units get the Platoon's passive bonus, and that Role's slot cap is raised. One uniform template replaces the bespoke Platoon Abilities, which also settles the undesigned ARMOR and SUPPORT ones. **Not yet decided:** the actual bonus each Role receives.
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
- **CORE is defined per Platoon, per faction.** Not every faction gets every Platoon (e.g. Saints barely field RECON, so need no RECON Platoon). Bonuses are deliberately asymmetric and should reinforce a faction's strength or slightly lessen one of its weaknesses (illustrations, not decisions: Regiments' infantry Platoon gets a massed-fire benefit; Oathkeepers' infantry Platoon gets a pre-game redeploy).
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

1. **Resolved (Round 3):** `Massed Ranks` *becomes* Regiments' Infantry-anchored Platoon's CORE bonus, rather than sitting alongside a separately invented one. It stops being granted faction-wide to any 8+-model unit and instead applies only to CORE-tagged, Infantry-keyword units within that specific Platoon (same internal "8+ models" condition on the unit itself, unchanged) — closing the overlap concern outright, since there's no longer a second, distinct bonus to overlap with.
2. **New, opened by the above:** `Massed Ranks` was also Imperial Regiments' faction-wide *signature trait* (one per faction, per `faction-identity.md`'s design rule). Moving it into a Platoon-gated CORE bonus vacates that role — **Regiments needs a new faction signature trait.** Deliberately deferred, not designed now.

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

Ten bodies, Wounds 1, Armor 4, Evasion 5, Speed 5, Mettle 4, **exactly** 100 points. That is the reference unit, the formula's calibration anchor, and the mental model for army size. *(Confirmed, not just asserted, by the rebuilt §11 formula — this unit is the anchor the constants were solved against, not a number that happened to come out right. The "1000-point list" framing itself is still open — see §11 — since the standard game's own point target hasn't been decided yet; that's independent of whether the anchor squad itself prices correctly.)*

Three rules follow, and they are anti-spiral rules:

1. **Every mechanic is evaluated by what it does to a rifle squad.** If a rule is neutral or confusing for line infantry and only makes sense for a five-model elite squad, it is the wrong rule.
2. **When an elite unit needs a new subsystem to function, the elite is wrong — not the game.** Elite units get better *stats* and better *weapons*, both of which the points formula already prices. They do not get compensation mechanics. If five Oathkeepers underperform ten riflemen at the same cost, their stat line is wrong, or their price is.
3. **New systems must justify themselves for the common case.** A rule introduced to solve an elite faction's problem has to also earn its place in a mirror match of line infantry, or it does not go in.

The failure mode this guards against is real and it compounds: each fix for an exceptional unit adds a subsystem, the subsystems interact, and the game ends up complicated in service of the units *fewest* players field.

### Resolved conventions

- **Mettle is additive and higher-is-better** — `2d6 + Mettle ≥ 10 + suppression markers` (re-anchored twice: d10 → d6 → 2d6; see §5). Every stat on the card now reads "bigger is better."
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

Common actions: **Move**, **Shoot**, **Fight**, **Rally** (remove all suppression markers from this unit), **Claim** (take an objective). **INFANTRY**-keyword units claim for free, spending no action to do so. Any other unit may still Claim, but only in place of Shoot or Fight — it cannot also make an attack that activation, though it may still Move (see §9). Some units get a free bonus action as a named exception — not a universal system.

No general reaction economy. Triggered abilities are written per-unit as exceptions.

## 2. Movement & Formation

No coherency stat. Move the leader model by its **Speed** stat, then place the rest of the unit within 2" of the leader, or within 2" of two models that are each within 2" of the leader (Warmachine-style reset — platoon "resets" every time the unit moves).

Engagement range: 1" baseline, extendable by weapon or trait.

## 3. The Dice Engine

**Every check is roll-over on a d6: meet or exceed the target number to succeed.** *(Converted from d10 — see the version note at the top of this document for why.)*

**Dice floor/ceiling, universal:** an unmodified **1 always fails**; an unmodified **6 always succeeds**. "Unmodified" means the raw face physically shown on the die — this check happens before any modifier is applied, whether that modifier lands on the target number (most traits) or directly on the roll itself (range bands, below). A natural 6 always succeeds even after a −1 range penalty; a natural 1 always fails even after a +1.

### The attack sequence

1. **To-hit** — roll d6 per attack die against the target's **Evasion**. Total dice = weapon's Attacks × models firing.
2. **Damage check** — each hit rolls again against the target's **Armor**, after **AP** is subtracted. Each success removes the weapon's **Damage** value from the target's **Wounds** pool.

**Critical Hit** — a hit roll of an unmodified 6 is a Critical Hit. On its own this changes nothing beyond the success it already represents under the floor/ceiling rule above — it's a named hook, not a bonus, and exists purely so traits can key off it (`Extra Hits`, `Negates (Critical Hits)`; see glossary). Deliberately no baseline effect for anyone: a universal "natural 6s also auto-wound" rule would let every weapon in the game ignore the AP scale on a flat ~17% chance regardless of how mismatched it is against the target's Armor, which undermines AP's whole job as "the only real answer to heavy armor" (below) — keeping the bonus trait-gated means only weapons built for that identity get it. `Anti-[Keyword]` is the deliberate, narrow exception to this principle — it grants a natural-6 auto-wound, but only against one named keyword a specific weapon was built to hunt, never universally (see glossary).

Higher Evasion = harder to hit. Higher Armor = harder to damage.

There is no attacker-side accuracy stat. To-hit difficulty is entirely defender-side; attacker differentiation comes from traits, rerolls, and Anti-[Keyword] weapons.

### Evasion — templated by archetype, not freely tuned

d6 only offers five meaningfully distinct values (2 through 6), which isn't enough room for the fine per-unit tuning the old d10 curve allowed. Evasion is now assigned by broad archetype template rather than hand-picked per unit — "Heavy Vehicle" and "Light Vehicle" below are weight-class labels within the Vehicle keyword, not keywords of their own:

| Archetype | Evasion | Hit chance |
|---|---|---|
| Heavy Vehicle | 2–3 | 83% / 67% |
| Light Vehicle | 3–4 | 67% / 50% |
| Infantry (baseline) | 5 | 33% |
| Elite / dedicated dodge specialists | 6 | 17% |

Evasion above 6 is reachable only through modifier stacking, never as a base value, and cascades exactly like Armor above 6 (below) once it happens. This is rare enough in practice that a known quirk of the cascade — Evasion 7 and 8 land on the *identical* ~14% chance (both reduce to "a natural 6, then anything but a natural 1") — isn't worth solving for. The same quirk is a real problem for Armor, immediately below, because AP makes it come up constantly rather than rarely.

**Veterancy no longer differentiates through Evasion.** A veteran and a rookie of the same archetype share the same defensive template; the gap between them has to come from Mettle, Armor, Speed, Wounds, equipment, and traits instead. *(The exact Mettle values a roster should span under the new die haven't been recalibrated yet — flagged in Open Threads.)*

### Armor above 6

Armor is **not capped at 6**. When a target's Armor after AP exceeds 6, an unmodified 6 no longer succeeds automatically — instead it buys a **second roll** against `Armor − 6`, cascading again if that also exceeds 6.

A hull at Armor 9 struck by an AP 0 weapon needs a 6, then a 3+: `1/6 × 4/6 ≈ 11%`. The same hull struck by an AP 3 weapon is rolling against a flat effective Armor of 6 — a straight `1/6 ≈ 17%`. Higher AP still means a meaningfully better chance to damage, exactly as intended; the curve continues smoothly instead of hitting a wall.

*(Mechanic unchanged from the d10 version — Marcher's original inspiration — just re-anchored to the smaller die.)*

### Armor's floor — the AP overkill cap

The same "two different numbers land on the identical probability" quirk that's harmless at Evasion's rare ceiling was a real problem at Armor's **floor**, and it wasn't rare: once AP dropped a target's effective Armor to 1 or below, any further AP was wasted against that target — Armor 1, 0, and −1 all resolved identically, and because AP subtracts from Armor on every attack, this came up constantly, not as an edge case.

**Resolved: AP can only reduce a target's effective Armor to a floor of 2.** `Effective Armor = max(Armor − AP, 2)`. This is the AP overkill cap the weapon-cost formula needed — the mirror image of the existing Damage overkill cap (`min(Damage, 2)` against soft targets, §11) — and it removes the quirk outright rather than smoothing it: there's no separate Armor 1 / 0 / −1 to land on identically, since the formula never lets effective Armor reach them. A Damage-1 weapon at AP8 against Armor 10 (`max(10−8, 2) = 2`) rolls a flat 2+, an 83% wound chance — heavy AP genuinely wins, all the way down. *(The pricing consequence is now resolved — §11 Step 2's soft/hard reference math applies this same floor directly.)*

### The AP scale (draft — needs playtesting-anchored calibration)

**AP is not capped at 4 — Armor can reach ~10, and with the floor-of-2 rule above, punching a heavily-armored target down to its floor genuinely needs the higher end of the scale.** An earlier pass compressed this table to 0–4 on the assumption that d6's narrower Armor range needed a narrower AP range too; that assumption no longer holds now that Armor isn't capped low either. Restored to the original 0–8 scale and its real-world reference pairings:

| AP | Reference | | AP | Reference |
|---|---|---|---|---|
| **0** | Modern assault rifle | | **5** | 76mm |
| **1** | Magnum rifle cartridge | | **6** | 88mm |
| **2** | 20mm autocannon | | **7** | Modern 120mm sabot |
| **3** | WWII 37mm | | **8** | Railgun |
| **4** | 57mm | | | |

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

> **Pricing consequence:** because every model has Fists, it is **free** — nobody pays for a capability every model already has by default, the same reasoning that used to justify TYPE/CATEGORY bundles being free (that specific precedent no longer holds — see §7, those bundles are individually priced now — but the reasoning for a truly universal default still does). Real melee weapons are priced at their **margin over Fists**, not their absolute value. Skipping this would charge every model twice for a capability it already had. *(Partially resolved — `CCW` (replacing `Fists`) is confirmed at a flat **0 points**, by decision rather than derivation: "it exists solely to give each unit a melee option," never run through the weapon formula at all. Still queued: this section's own prose still says `Fists`, and the "69% of a Bayonet" comparison figure hasn't been recomputed against the new formula — a real weapon now, priced normally, not "margin over CCW" since margin over zero is just its own value.)*

## 5. Morale — Determined → Shaken → Frozen → Routing

### The Mettle check

```
Roll 2d6 + Mettle.  Pass if the total ≥ 10 + suppression markers held.
```

An unmodified roll of **2 always fails**; an unmodified **12 always passes** — the same floor/ceiling principle as the main d6 engine (§3), just on the wider die pool this check uses. Higher Mettle is better, like every other stat on the card. A unit with Mettle 4 holding two markers needs an 8+ on 2d6, a 42% chance *(re-anchored twice, d10 → d6 → 2d6 — see the Decision Queue for why a flat d6 stopped differentiating Mettle values at all. The actual Mettle values a roster should span under 2d6 still need a recalibration pass — see Open Threads)*.

- **Pass** — remove **one** suppression marker.
- **Fail** — step **up** one level on the track.

**Check timing:** at the start of a unit's activation if it holds any markers, or immediately when an effect forces one.

**Naming note:** this specific check — the one that can step a unit up the morale track — is a **Morale test**. The same underlying roll (2d6 + Mettle vs. a target number) is reused for other, unrelated triggered effects (`Rallying Cry`, `Combat Medic`, `Divine Favor`, etc.); those are **Mettle checks**, not Morale tests. The distinction matters because some traits (`Mindless`, `Undaunted (X)`) specifically reference Morale tests only — they don't touch a unit's other Mettle-gated abilities.

### Suppression markers

Dealt by weapons and effects (see **Suppressing**). **Markers persist until removed.** They do not clear at end of round.

Three ways to be rid of them, none punishing:

| Method | Removes |
|---|---|
| Passing a Mettle check | 1 marker |
| The **Rally** action | *all* markers on this unit |
| A trait or ability written to do so | as written on the granting rule |

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
| **Shaken** | −1 Evasion, −1 Armor only. *(No longer worsens Mettle too — that stacked with the suppression-marker penalty on the exact same check the marker already makes harder; markers alone now carry the rising difficulty.)* |
| **Frozen** | Shaken's penalties, **and no Move actions.** Can still Shoot and Fight. |
| **Routing** | Must spend its entire activation moving toward the nearest board edge. Reaching it removes the unit from play. |

**Vehicles** run the same four steps but end in **Destroyed** rather than Routing.

**Damage Track** *(single-model units only, uncosted — a universal rule, not a purchasable trait)*: the first time this unit's Wounds drop below half its starting total, it immediately makes a Morale test — this is a genuinely separate trigger from the marker-driven one above, and can still step the unit down the track as normal if it fails. Regardless of that test's outcome, the unit also permanently suffers **−1 to all Attack Rolls and Wound Rolls it makes**, for the remainder of the game, representing damage to its systems, organs, or components. This exists *alongside* the marker-driven track above, not in place of it, and the two are deliberately built to never overlap on the same axis: Shaken/Frozen only ever touch Evasion, Armor, and Move actions, so a suppressed *and* half-dead single-model unit is worse off than either alone — genuinely compounding penalties, not double-counting the same one under two names.

**Courage** re-rolls failed Mettle checks. **Fearless** ignores suppression markers on Mettle checks — the two are deliberately separate, reusable pieces rather than one bundled trait.

**`Aura of Discipline`** *(Aura, 12")* — as an action, this model may make a Mettle check; on a pass, every friendly unit within 12" of it (including its own) discards all suppression markers. "Protect your officers, hunt theirs" — a real risk/reward swing, not a passive: it costs the leader's own action, it can whiff on a failed roll with nothing to show for it, and losing the leader denies the whole effect outright. Deliberately just `Rallying Cry` widened from "self only" to the aura, reusing the game's existing infrastructure twice over rather than inventing anything new — the already-formal `Aura (12")` category (Aura of Courage, Aura of Warding, Reliquary) supplies the range, `Rallying Cry`'s own shape (Mettle test, full clear on a pass) supplies the mechanism. *(Priced now that §11 Step 5's ability tiers exist — **Major (15)**, given it can affect every friendly unit in range at once, not just the leader's own, comfortably clearing `Rallying Cry`'s own likely Minor tier for the self-only version.)*

**Doctrine shift, not yet priced:** `Fearless`, `Undaunted (X)`, and `Mindless`'s own immunity clause are moving from "a common menu option any unit might take" to **rare, expensive, and faction-signature** — Cultists get `Mindless`, Wrathful Oathbreakers' Marine-chassis units get `Fearless`, and so on, rather than any unit being able to buy suppression-immunity off a shared list. The actual re-pricing is deferred to the points-formula rebuild; this is a standing design instruction for that pass, not yet acted on.

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

### Facing & Arcs

Only matters for models that need it — anything carrying `Armored Front` or an Arc-restricted weapon (`Frontal/Rear/Side Arc`, `Traversing`). Infantry never tracks facing; True Line of Sight already governs what it can see and be seen by.

**Setting facing:** a model faces a single direction, set at deployment. It may re-orient to face any direction at the end of a Move action, whether or not it actually moved — there's no requirement to end a move facing the direction of travel.

**The four arcs**, measured from the center of the model's base, relative to its facing: **Front** is the 90° wedge centered on that facing (45° either side of straight ahead); **Rear** is the mirrored 90° wedge directly behind; the remaining 180° splits evenly into a **Side** arc on each flank.

**Two separate checks, easy to conflate:**

- **`Armored Front`'s AP modifier** is about the *target's* arc — measure from the target's own facing to the attacker's position. Front reduces incoming AP by 1, Rear increases it by 1, Side is unmodified. This is checking how exposed the target's hull is, nothing to do with the shooter.
- **An Arc-restricted weapon** (`Frontal/Rear/Side Arc`, `Traversing`) is about the *bearer's* own facing — the weapon can only target something that falls within its stated arc as measured from where its own hull (or turret, for `Traversing`) is currently pointed. This is checking whether the gun can physically point at the target at all, nothing to do with the target's own facing.

A vehicle can easily be in a situation where both checks apply at once and give different answers — its own gun might not be able to traverse onto a target that's well within its `Armored Front` rear arc, for instance. That's intentional: the two rules are answering genuinely different questions.

*(First pass, written to unblock playtesting — closes Open Thread #8. Deliberately doesn't handle every corner case; the shape above should cover ordinary play.)*

## 7. Role and Keywords

Every unit carries one **Role** and any number of **Keywords**. This replaces the old TYPE/CATEGORY split — the two concepts survive, but only one of them still grants anything by itself.

### Role — the force-org slot

One per unit, from the same six names CATEGORY used: **ARMOR, COMMAND, LINE, RECON, SHOCK, SUPPORT.** Role is a **list-building label only — it grants no rules.** It fills a Platoon slot (§8) and nothing else. A unit's Role should reflect what it's actually expected to do on the battlefield; auditing the existing roster against that standard is separate, ongoing work, not resolved here.

### Keywords — what a unit *is*

Any number per unit. Keywords **do nothing on their own.** They exist for two reasons:

1. **Sharpen targeting** — `Anti-[Keyword]`, "an allied RECON unit," "choose a friendly [X] unit to…" A rule can reference a unit's Role exactly the same way it references a Keyword; nothing requires the target of such a check to be a Keyword specifically.
2. **Design-time convenience** — certain traits are conventionally *paired* with certain Keywords when a unit is built (a Vehicle-keyword unit usually takes `Armored Front`; a Monster-keyword unit usually takes `Terrifying`), but that pairing happens at the drawing board, not the table. A keyword grants nothing automatically at runtime.

The foundational Keywords — the ones every unit reaches for first — are the same six TYPE used: **Infantry, Cavalry, Vehicle, Monster, Aerial, Towable.** The set is open-ended beyond that: a new Keyword can be invented whenever a rule needs one to reference (`Caster` already works this way — see glossary — and a future `Mech` keyword is a live example of the kind of thing this is for).

In the data, every unit still takes one Role plus its Keywords — e.g. the APC is Role **SUPPORT**, Keyword **Vehicle**; the AFV is Role **ARMOR**, Keyword **Vehicle**; the Regimental Officer is Role **COMMAND**, Keyword **Infantry**.

### The one automatic exception: INFANTRY and objectives

Claiming an objective is the single place a Keyword still triggers a rule by itself, because it's core infrastructure for the whole combined-arms design (§9), not a bundled convenience a unit builder opts into: **a unit with the INFANTRY keyword claims an objective for free. Every other unit may still claim, but only by spending its Combat action to do so** (see §1). This deliberately follows the Keyword itself, not the Role — a Transport inheriting a LINE Role from its cargo (§10) does not thereby claim for free; the cargo does, because the cargo is what's actually Infantry.

### Traits that used to be automatic, now individually priced

Everything below used to be bundled for free onto a TYPE or CATEGORY. None of it is automatic anymore — a unit has one of these only if it was built with it, paying whatever the trait's Minuscule/Minor/Major tier costs (§11 Step 5, which now has a first-pass classification for this exact list). This table is kept as design-time guidance for which trait conventionally answers which Keyword or Role — not a grant table.

| Commonly paired with | Trait(s) |
|---|---|
| Infantry (keyword) | `Entrenched` |
| Cavalry (keyword) | `Run Them Through`, `All-Terrain` |
| Vehicle (keyword) | `Armored Front`, `Hardpoints` |
| Monster (keyword) | `Terrifying` |
| Aerial (keyword) | `Flying`, `Soaring Above` |
| Towable (keyword) | `Trailor`, `Emplaced Weapon` |
| ARMOR (Role) | `Bulwark`, `Hardpoints` |
| COMMAND (Role) | `Leadership Aura` |
| LINE (Role) | — *(its old grant, `Boots on the Ground`, is gone outright — that benefit now follows the INFANTRY keyword directly, per the exception above, not any Role. A LINE-Role unit that isn't Infantry gets nothing from LINE itself.)* |
| RECON (Role) | `Spotter`, `Camouflaged`, `All-Terrain` |
| SHOCK (Role) | `Brutal Assault` |
| SUPPORT (Role) | `Where We're Needed` |

`Flying` is written as its own standalone entry (see glossary) rather than an Aerial-exclusive bundle item — anything can be granted `Flying` on its own (see `Jump Jets`); Aerial is just the keyword it's conventionally paired with. `Soaring Above` is what actually distinguishes a true aircraft from anything else that merely has `Flying`.

> **Note, superseding the old one below:** `Impact(X)` is **back**, in a genuinely new shape — not a restoration of whatever the original v0.3 draft meant by it. See the trait glossary's `Impact (X)` and `Crushing Impact (X)` entries. `Fear` is still gone; the Monster signature stays `Terrifying`. Cavalry's baseline charge bonus stays `Run Them Through` — `Impact (X)` is a separate, optional trait some Cavalry (and Infantry, and vehicles/monsters via `Crushing Impact`) carry on top of it, not a Keyword-wide replacement.

## 8. List Building — Platoons

Platoon slots are defined directly by Role. The data currently defines a **Vanguard Platoon** force entry that accepts all Roles with **no min/max constraints set** — slot limits are not yet encoded.

**Proposed base spread** (not yet in the data):

| Role | Min/Max |
|---|---|
| COMMAND | 1 |
| LINE | 2–4 |
| RECON | 0–2 |
| SHOCK | 0–2 |
| ARMOR | 0–2 |
| SUPPORT | 0–2 |

### CORE and the Platoon bonus

Choosing a named Platoon designates a **CORE** Role *or* Keyword for that list — both are on the table, and the one worked example below actually resolves as a Keyword, not a Role. Two things follow from being CORE:

- **The Platoon's anchor Role's slot cap is raised**, mirroring the old spread shift (anchor expands toward 2–4, everything else tightens). Slot caps are always a Role concept — the base spread above is keyed by Role — so even a Keyword-designated CORE still has an associated anchor Role whose cap loosens.
- **Only units that satisfy the CORE designation gain the Platoon's passive bonus**, checked against whichever axis — Role or Keyword — that specific Platoon names. One uniform *template* replaces the old bespoke per-Platoon abilities (`Hold Fast`, `Break the Line`, `Fast as the Wind`), which also retires the old "ARMOR/SUPPORT abilities are undesigned" gap outright — there's no longer a shared generic ability left undesigned for any Role; every bonus is faction-specific from the start.

**The bonus itself is defined per Platoon, per faction — deliberately asymmetric, and not every faction offers every Platoon.** Saints barely field RECON, so they don't need a RECON-anchored Platoon at all. A bonus should reinforce the faction's own strength or slightly blunt one of its weaknesses, never read as a generic, faction-neutral effect.

**Platoon names are faction-specific, drawn from that faction's own fluff — there's no shared archetype vocabulary any faction reaches for by default.** Regiments' Infantry Platoon doesn't have to be called anything a Saints or Oathkeepers infantry-anchored Platoon would also call itself; the old generic names (`Line Formation`, `Spearhead`, `Outrider`) don't carry forward as reusable labels.

**The first worked example, and so far the only one: Regiments' Infantry Platoon designates CORE as the INFANTRY *keyword*, not the LINE Role.** Its bonus is `Massed Ranks` (see faction-identity.md): while a CORE, Infantry-keyword unit in that Platoon holds 8 or more models, it re-rolls Attack Rolls of 1 and gains +1 Mettle.

**Confirmed, 2026-09-28: every faction identity has two separate layers, not one.** (1) One **faction-wide signature trait** — always on, no Platoon required (`Oathbound`, `Bound Spirit`, `Martyrs, all`, `Wrathbound` — see faction-identity.md). (2) One or more **Platoon-specific CORE bonuses** — only live when that Platoon is chosen, only benefiting CORE-tagged units within it. These are parallel, not substitutes: a faction can have one without the other being done yet, which is exactly Regiments' situation right now — CORE bonus done (`Massed Ranks`), faction-wide signature trait now empty (moving `Massed Ranks` out of that role vacated it) and needs a replacement. The other four factions are the mirror image: faction-wide signature trait intact, CORE bonus undesigned (their old Doctrines are retired — see faction-identity.md's per-faction Doctrine lines, struck through).

### Embedded units

The data implements embedding directly. A **Rifle Squad** may take:

- **Embedded Leader** — one Regimental Officer (or any COMMAND-Role leader unit), which then counts as LINE rather than COMMAND.
- **Embedded Heavy Weapon Team** — one Heavy Weapons Team, which is stripped of SUPPORT and re-categorized as LINE.

Embedding therefore **changes the host's Role** to match the squad, so an embedded model doesn't consume its own slot.

### Army scaling

1 Platoon per 500 points, minimum 1 Platoon per 1000 points. Activation count is simply unit count; Pass Tokens handle asymmetry.

**No resource economy.** Confirmed — Marcher's Supply/Intel stays in Marcher.

## 9. Missions & Combined Arms

Objective-based scenarios, varied deployment styles. Alternating activation; the round ends when every unit has activated.

**Combined arms is a primary design goal, not a theme.** Role caps shape what a list *contains*; the three rules below make a mono-arm list *lose*, which is the part that actually matters.

### 1. Objectives need boots

**Any unit may claim an objective — the old hard "Vehicle/Monster/Aerial can only contest, never score" restriction is gone** (§7): a unit with the INFANTRY keyword claims for free; any other unit may still claim, but only by spending its Combat action to do so, giving up its attack that activation.

**That's no longer a wall, but it's still a real, felt tax — and it lands hardest on exactly the lists least able to afford it.** A tank holding a marker is a tank not shooting that activation, full stop; nothing else on the table converts firepower into board control that directly. And because armor is expensive, an armor-heavy list fields *few* units to begin with (§11 Step 4) — pulling one off the firing line to babysit an objective is a proportionally bigger bite out of that list's total output than the same trade is for an infantry-heavy list, which has bodies to spare precisely because they're cheap. **Every army therefore still benefits enormously from fielding infantry** — not because other arms are structurally locked out of scoring anymore, but because infantry is the only arm that ever does it for free. A mono-arm armor list can grind out objectives if it's willing to stop shooting to do it; that's a real, meaningful cost, just no longer an impossible one.

### 2. Terrain density is a rule, not a suggestion

A standard 4'×4' board carries **at least 8 terrain pieces**, of which:

- **3 or more** carry `Difficult`, `Impassable`, or `Void` — ground armor cannot cross freely
- **4 or more** carry `Blocking` — firing lanes are earned, not given

A board failing this is not a legal board. Sparse terrain silently converts the game into a shooting contest, which is the failure mode that kills combined arms.

### 3. Anti-armor must actually kill armor

Dedicated anti-armor weapons need to threaten the heaviest chassis fielded (currently Wounds 14–18 on Wolverine/Badger/Bastion, not the Wounds 10 this section originally assumed). Massed armor should be a **trap**, punished by a comparatively cheap specialist. `Anti-[Keyword]`'s guaranteed bonus damage on a natural 6 (see glossary — no longer a hit-doubling rule) supplies the machinery; the stat lines have to honour it.

### The intended shape

Each arm needs a job the others cannot do:

- **Infantry** takes and holds ground — the only arm that ever does it for free.
- **Armor** breaks through and denies; it can hold too, but only by giving up its firepower to do it.
- **Artillery** kills at range, is blind without RECON, and is helpless up close.
- **Recon** sees for the artillery and cannot fight.
- **Aerial** strikes anywhere; it can claim like Armor can, at the same cost, but its whole point is reaching what infantry can't yet, not camping on what it already has.

Dependencies, not merely roles. Artillery genuinely does not function without a Spotter, and that coupling is the model for everything else.

### A first mission — Claim the Ground

Written to unblock playtesting, not to be the final word — one working scenario out of the 5–10 eventually planned. Leans entirely on mechanics that already exist; invents nothing new.

- **Board:** 4'×4', meeting the terrain-density minimum above.
- **Objectives:** 5 markers — one at the exact center, the other four each 18" out from center along the board's diagonals. Symmetric for both players.
- **Deployment:** opposing long edges, each player within 12" of their own.
- **Length:** 5 rounds.
- **Scoring:** at the end of each round, an objective is **controlled** by a player if they have a unit that took the Claim action on it that round, and no enemy unit is within 3" of it. Each controlled objective scores its controller 1 point.
- **Win condition:** most points after 5 rounds. Tied on points: whoever has more surviving Wounds across their whole army wins. Still tied: a draw.

*(The 3" contest range is a first guess, not derived from anything — flag it the same way as every other hand-tuned constant in this document if it plays oddly.)*

## 10. Transports

**Transport(X)** where X is a **seat** capacity, not a model count. *(Changed 2026-09-28 with the introduction of the Size stat — see the Reference section below. Before Size existed, one model always consumed exactly one unit of capacity; now a model consumes as many seats as its own Size value.)* A unit's total seat cost when embarking = its own Size × however many models are boarding — `Transport (14)` carries 14 Size-1 troopers, or 7 Size-2 Marines, or a mix (8 Size-1 + 2 Size-3 is exactly 14 seats). Defined values in the data: `Transport (6)`, `(11)`, `(14)`, `(28)`. The APC is `Transport (14)`.

**Eligible cargo:** Infantry and Cavalry, by keyword — but this is necessary, not sufficient. **Cavalry is Size X by blanket convention** (see Reference — Unit Profile), so no Cavalry unit can actually ever embark regardless of this keyword rule; only Infantry does in practice.

### Dedicated Transports

A Transport may be taken as a **Dedicated Transport** attached to one specific eligible unit during list building. A Dedicated Transport:

- **Takes the Role of the unit it carries.** A transport carrying a LINE squad *is* a LINE unit, for every rules purpose that checks Role — `Anti-[Keyword]`, Platoon/CORE eligibility (where a Platoon's bonus isn't Keyword-restricted — see §8), doctrine effects, all of it. It does **not** inherit the cargo's Keywords — a transport carrying Infantry doesn't itself become Infantry (see §7's INFANTRY/objectives exception).
- **Does not consume an additional slot** beyond its payload's.
- Must **deploy carrying that unit**, and may never carry a different one.
- Still counts as its own unit for activation and Pass Token purposes.

*(Slot treatment carried over from Marcher, which allots transports "1 per Transport-Eligible Unit" rather than making them compete with combat choices.)*

Transports competing for Role slots quietly kills combined arms. Under tight caps — Oathkeepers hold SUPPORT 0–1 — buying a transport spends the slot that would have held fire support, so the rational choice is always to walk. This makes mobility a **points** decision rather than a slot decision, which is the one that should govern it.

**Inheriting the payload's Role is what keeps that honest.** A slot-free transport with no Role would be a free unit with no downside; instead it is a fully exposed member of the platoon it serves. Choosing what a vehicle carries chooses what it is vulnerable to — an Oathkeeper gunboat full of LINE infantry is hunted by `Anti-Line`, while a pure tank in the ARMOR slot is hunted by `Anti-Armor`. Two genuinely different threat profiles, chosen at list building.

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

**Rebuilt from a bare slate 2026-09-28** — every constant and table below is new, re-derived for d6 rather than patched from the d10-era formula. `points.py` has not been updated to match yet; this section is currently ahead of the code. **Not yet done: re-costing the actual roster against this formula** — every unit's price in `factions/imperial_regiments.json` and every `.cat` file is still a stale d10-era number until that separate pass happens.

**Target scale:** a standard game's point total is open again (1000 vs. 2000 vs. 3000 — see the Decision Queue); nothing below depends on that number, since the formula prices one model or weapon at a time.

Model cost and weapon cost are computed **separately** and summed, because Evasion is a property of the target rather than of the attacker or its weapon — the two halves genuinely don't interact. Every Role/Keyword bundle trait (§7's reference table) that used to be a free grant is now individually priced through Step 5, not absorbed into the baseline.

### Step 1 — Model cost

```
Model Cost = BASE_MODEL × Wounds × E(Evasion) × A(Armor) × S(Speed) × M(Mettle)
BASE_MODEL = 6.45
```

**E and A** are `sqrt(1/P)` against the *true* combat probability (the Armor cascade mechanic, §3, is unchanged and still governs actual play — it's just not mirrored 1:1 into cost, since doing so made a Bastion-grade chassis price over 2000 points on the chassis alone). The square root is what tames that: it keeps the "durability costs superlinearly" principle intact while stopping it from exploding at vehicle-scale Armor.

| Evasion | 2 | 3 | 4 | **5** | 6 |
|---|---|---|---|---|---|
| **E** | 0.63 | 0.71 | 0.82 | **1.00** | 1.41 |

| Armor | 2 | 3 | **4** | 5 | 6 | 8 | 10 | 12 | 14 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | 0.78 | 0.87 | **1.00** | 1.23 | 1.73 | 1.90 | 2.45 | 4.24 | 4.65 | 10.39 |

Both normalised to the anchor's own stats (Evasion 5, Armor 4) rather than an arbitrary reference — Evasion 5 is now literally the Infantry archetype baseline (§3), not a separate hand-picked pairing.

**M (Mettle)** gets the same `sqrt(1/P)` treatment, but priced off **P(fail)** on the 2d6 Morale check (§5), not P(pass) — a natural mistake to make and worth flagging: Mettle's *good* outcome is passing, the opposite direction from Evasion/Armor where the attacker's *bad* outcome (missing, failing to wound) is what the target wants. Pricing off `1/P(pass)` makes higher Mettle cheaper, which is backwards.

| Mettle | 1 | 2 | 3 | **4** | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| **M** | 0.62 | 0.69 | 0.82 | **1.00** | 1.29 | 1.83 | 3.16 |

**S (Speed)** has no probability basis — movement doesn't map onto a hit or wound chance — so it stays a hand-tuned ladder, same status as Mettle's marker-check rate used to be. Zero-anchored, not baseline-anchored, since true immobility is a real, separate liability from merely being slow:

```
Speed 0:  S = 0.70   (a discrete "Immobile" tax, not a continuation of the curve below)
Speed 1:  S = 1.00   (the free/neutral reference point)
Speed N≥1: S = 1 + 0.06 × (N − 1)
```

| Speed | 0 | 1 | 2 | 3 | 4 | **5** | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| **S** | 0.70 | 1.00 | 1.06 | 1.12 | 1.18 | **1.24** | 1.30 | 1.36 | 1.42 | 1.48 |

Anchor stats are Evasion 5, Armor 4, Speed 5, Mettle 4 — a plain grunt, who costs **exactly 8.00** (the 80/20 split's chassis target; see The currency scale, below).

> **Why the terms multiply rather than add.** Unchanged reasoning from the old formula: being good at *everything* has to cost superlinearly, or elite units are undercosted by construction. An elite unit's cost genuinely is its downside — most units cannot afford to be fast *and* armored *and* tough at once, and that's the intended pressure.

> **Armor's floor is a real combat rule, not just a pricing trick.** §3 already establishes `Effective Armor = max(Armor − AP, 2)` — AP can never push a Wound Roll easier than a flat 2+. That floor is what keeps the Armor factor table above from needing its own separate overkill handling.

### Step 2 — Weapon cost

```
Soft = Attacks × P_hit(Evasion 5) × P_damage(Armor 4, AP) × min(Damage, 1)
Hard = Attacks × P_hit(Evasion 3) × P_damage(Armor 8, AP) × Damage
Value = (Soft + Hard) ÷ 2
Weapon Cost = BASE_WEAPON × Value × R
BASE_WEAPON = 12.857
```

Reference targets are now tied to real archetypes instead of an arbitrary pairing: **soft = the anchor's own Infantry stat line** (Evasion 5 / Armor 4 — no longer a separate invented reference, it's literally what Infantry means under §3's template), **hard = Heavy Vehicle** (Evasion 3 / Armor 8, already deep enough to engage the real cascade mechanic).

**The overkill cap is `min(Damage, 1)`, not 2** — the anchor's real Wounds is 1, so anything above 1 is exactly as wasted against it as Damage 8 would be. The old cap of 2 was quietly overvaluing every Damage-2+ weapon's soft-target performance.

**The old "penetration × volume premium" term is dropped entirely.** It was compensating for a flaw the d10 formula had that doesn't exist here: `Value` already multiplies `Attacks × P_damage(AP)` *inside itself*, against both reference targets — that's already the real multiplicative relationship the premium term was trying to bolt on separately. Keeping both was double-counting the same effect. (Verified this wasn't just a hunch: a Heavy Machine Gun's "most expensive infantry weapon" status survives the term's removal — it now lands at a real, defensible ~9× the Rifle from its actual combat output alone, not ~17× inflated by a redundant multiplier.)

**Range multiplier R** = `0.6 + Range ÷ 30`, with melee at **0.85** — carried forward unexamined. This one doesn't connect to the Close/Effective/Long band mechanic (§3) at all; it's a separate "longer reach is worth more" assumption that hasn't been re-derived. Flagged, not fixed.

| Range | R | | Range | R |
|---|---|---|---|---|
| Melee | 0.85 | | 24" | 1.40 |
| 6" | 0.80 | | 30" | 1.60 |
| 12" | 1.00 | | 36" | 1.80 |
| 18" | 1.20 | | | |

**Worked example — a plain Rifle (A1/AP0/D1/18"):**

| Step | Value |
|---|---|
| Soft (vs. Evasion 5/Armor 4) | 1 × 0.333 × 0.500 × 1 = 0.1667 |
| Hard (vs. Evasion 3/Armor 8 — cascades: 1/6 × 5/6) | 1 × 0.667 × 0.139 × 1 = 0.0926 |
| Value | (0.1667 + 0.0926) / 2 = 0.1296 |
| R (18") | 0.6 + 18/30 = 1.20 |
| **Cost** | 12.857 × 0.1296 × 1.20 = **2.00** |

The Rifle is the calibration anchor itself — `BASE_WEAPON` was solved so this lands on exactly 2.00 (80/20 split), not discovered to land there.

#### `Anti-[Keyword]` pricing

```
Anti-X surcharge = BASE_WEAPON × R × 0.5 × Attacks × (1/6) × [min(Damage,1) if the keyword is soft-type, else Damage if hard-type]
```

Added on top of the weapon's normal cost, not multiplied into it. Three things make this correct rather than just plausible-looking:

- **Matched to the actual keyword.** `Anti-Infantry` prices only against the soft reference, `Anti-Vehicle`/`Anti-Armor` only against hard — never blended, since the bonus (see glossary — a guaranteed hit on a natural 6, bypassing Armor and AP entirely) only ever triggers against one or the other. It needs no `P_hit`/`P_damage` lookup at all, since a natural 6 always hits regardless of the target's real Evasion, and the bonus skips the Wound Roll.
- **Same overkill cap as the base formula** — the guaranteed bonus is exactly as wasted against a 1-Wound target as a normal hit would be.
- **The `× 0.5` weight is borrowed from the base formula's own soft/hard split**, not a new invented discount — `Anti-Infantry` only pays off on the half of encounters the base formula already assumes are soft-target ones.

Verified against a fair benchmark (the cost of doubling the weapon's own Attacks — a true dice-for-dice comparison, since the bonus can trigger off every one of a weapon's existing attack dice): every case checked lands at 0.28×–0.67× of that benchmark, confirming `Anti-[Keyword]` really is the cheaper route to a specific-target tool it was always meant to be.

### Step 3 — Weapon traits: Minuscule / Minor / Major

Replaces the old two-tier (bonus/restriction) system with one three-grade scale, graded by **how much a trait shifts the math of the attack, or whether it changes a unit's state as part of resolving it** — a state change (a marker, a forced check) counts the same as a probability shift even when it doesn't touch the attack's own numbers at all.

| Tier | Bonus | Restriction |
|---|---|---|
| Minuscule | ×1.05 | ×0.95 |
| Minor | ×1.15 | ×0.85 |
| Major | ×1.35 | ×0.65 |

First-pass classification (not exhaustive — refine as more traits get built):

- **Minuscule bonus**: `Accurate`, `Pistol`, `Armored Front` (cuts both ways — usually facing the enemy, but the rear weakness is real)
- **Minor bonus**: `Suppressing` (a real state change to the target, no math shift on this attack), `Optics`, `Onslaught`
- **Major bonus**: `Guided` (replaces Evasion outright), `Linked-Weapon` (rerolls every miss), `Indirect` (removes the LOS requirement entirely), `Overcharge`
- **Minor restriction**: `Traversing`, `Coaxial`
- **Major restriction**: `Heavy`, `Frontal/Rear/Side Arc`, `Consumable (1)`

`Anti-[Keyword]` sits outside this system entirely — see its own pricing above, not a tier multiplier.

**Multiple traits still compound, not add** — unchanged principle from the old formula, and the same reasoning holds: specialization is the theme of the weapon tiers, and compounding discourages loading one weapon with everything.

### Step 4 — Unit size scaling

```
Unit Cost = Model Cost × N
```

**No discount for larger squads.** The old sublinear `(N/10)^−0.15` Size Factor is retired outright — confirmed 2026-09-28, "no discounts, we'll address it with single-model damage scaling separately." Single-model toughness (vehicles, monsters) is no longer bought through an ever-larger Wounds stat multiplying into an ever-larger cost — it's handled by the **Damage Track** (§5) instead, a mechanic rather than a pricing curve.

### Step 5 — Named abilities: flat, not multiplicative

Same logic as before: an ability is a capability, not a modifier on an existing base, so it gets a flat cost rather than a multiplier. Now **three** tiers instead of two, matching Step 3's naming, anchored off `BASE_MODEL` rather than derived from probability (there's no clean probability basis for "how much is an aura worth," same status as Speed's coefficient):

| Tier | Cost | Roughly |
|---|---|---|
| Minuscule | **2** | ~30% of a grunt's chassis |
| Minor | **6** | ~1 grunt's chassis |
| Major | **15** | ~2.3 grunts' chassis |

First-pass classification of §7's "commonly paired, now individually priced" trait table:

| Trait | Tier |
|---|---|
| `Leadership Aura`, `Bulwark`, `Flying`, `Soaring Above` | Major |
| `Spotter`, `Entrenched`, `Run Them Through`, `Brutal Assault`, `Terrifying`, `Hardpoints` | Minor |
| `Camouflaged`, `All-Terrain`, `Where We're Needed`, `Trailor` | Minuscule |

`Armored Front` and `Emplaced Weapon` don't belong on this ladder at all: `Armored Front` is priced under Step 3 (it's a weapon-facing effect, graded Minuscule bonus above), and `Emplaced Weapon` is a genuine restriction — it belongs with `Conscript`/`Mindless` in the cost-*reducing* trait family, not this bonus-ability table.

These sit **outside** Step 4's unit-count multiplication — they usually attach to one model (a leader's aura), not the whole squad.

### Other surcharges

- **`Transport(X)`** — `X × 0.5` points, where X is now measured in **seats** (§10, Reference — Unit Profile's Size stat), not models. Deliberately *not* forced through the 80/20 model/weapon split — capacity is neither chassis durability nor a weapon, it's a third kind of value (pure delivery convenience), so it gets its own rate. No clean probability derivation exists for this one either; `×0.5` is a reasoned starting guess (roughly, 14 seats costs a bit more than one grunt's own chassis — a fair trade for potentially saving an entire squad a full activation of exposure), not a discovered number.

### The currency scale

`BASE_MODEL` (6.45) and `BASE_WEAPON` (12.857) move **together** and are calibrated at the **80/20 split**: the anchor unit — a 10-model Rifle Squad, `CCW` only, no bayonet by default — lands on exactly **100 points** (80 chassis + 20 weapons, 10 models × 8.00 chassis + 10 × 2.00 Rifle). `CCW` itself is **0 points**, fixed by decision rather than derived — "it exists solely to give each unit a melee option," not something the weapon formula prices. 70/30 remains a fully viable alternative (`BASE_MODEL` would become 5.65, `BASE_WEAPON` 19.29, Rifle 3.00) — nothing in either formula gives a technical reason to prefer one split over the other; 80/20 was kept because it's what was already decided, not because 70/30 broke anything.

### Validation

**Not yet re-run in full.** The old validation table (Imperial Regiments' 11-unit placeholder roster) was entirely d10-era output and has been removed rather than left to mislead — every number in it predates this rebuild. `points.py` itself now matches this section (rebuilt and hand-verified 2026-09-28), and a 5-unit watered-down slice of Imperial Regiments has been re-priced against it (Open Threads, item 11) — the full roster re-price is still separate, not-yet-finished work.

---

## Reference — Stat & Weapon Templates

### Unit Profile

`Speed | Mettle | Evasion | Armor | Wounds | Size`

- **Speed** — inches of movement.
- **Mettle** — morale. Additive, higher-is-better (see §5).
- **Evasion** — attackers roll ≥ this to hit. Higher is better for you.
- **Armor** — attackers roll ≥ this (after AP) to damage. Higher is better for you.
- **Wounds** — the wound pool: how much damage a model can absorb before it's removed. *(Briefly renamed "Toughness" during the v0.5 pass to avoid reading like a duplicate of "a wound," the individual unit of damage — reverted back to "Wounds," since that reads more like a hit-point pool at a glance and the `.gst`'s own characteristic field was still called `Wounds` the whole time regardless.)*
- **Size** — how many Transport seats one model occupies (§10). **1** = baseline infantry, **2** = Power-Armor-tier elites, **3** = Terminator-tier heavies, **X** = cannot embark in any Transport, full stop. Only ever stated on Infantry-keyword units — every Vehicle, Monster, and Aerial-keyword unit is implicitly Size X without needing it written down, and **Cavalry is Size X by blanket convention** (confirmed 2026-09-28: no Cavalry-coded unit across comparable wargames meaningfully benefits from Transport eligibility, so it's kept out going forward rather than judged case by case). This means §10's "Eligible cargo: Infantry and Cavalry" line is now necessary-but-not-sufficient — Cavalry remains keyword-eligible in principle, but Size is the real gate, and no Cavalry unit will ever actually pass it.

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
- **Caster** — a standalone Keyword, independent of Role and the foundational Keywords, granted to specific models (priests, psykers, sorcerers, and other channel-a-power archetypes) rather than defining a new TYPE or CATEGORY of its own — the same "anything can be granted it" pattern already established for `Flying`. Exists primarily so `Anti-Caster` has something to target; the actual casting/power mechanics a Caster-tagged model might use are undesigned and out of scope for now.
- **Anti-[Keyword]** — generalizes to any Keyword, not a fixed list. Whenever this weapon's Attack Roll against a target with [Keyword] is an unmodified 6, it immediately deals its Damage value to that target's wounds — no Wound Roll made for this portion, so it bypasses Armor and AP entirely (still reduced by flat damage-mitigation like `Bulwark`, and nullified the same as any other Anti-[Keyword] effect by `Negates ([Keyword])`). The attack then resolves normally on top of that — the Attack Roll was already a hit (natural 6 always hits), so it still gets its own ordinary Wound Roll exactly as any other successful hit would. *(Replaces the old ×2-hits-on-success rule entirely — chosen because it's the only shape of "explosive on a hot roll" that guarantees a crit against the right target is never a dud; see the Decision Queue, Round 3, for the three alternatives it beat out. Two separate hits now land on a natural 6 against a matching keyword — the guaranteed one and the normally-resolved one — and each is free to land on a different model in the unit via the standing one-hit-per-model allocation rule; no bespoke spillover clause needed. **Pricing:** §11 Step 2 — a flat additive surcharge on top of the weapon's normal cost, not a multiplier.)*
- **Bulwark** — reduce incoming damage by 1, to a minimum of 1.
- **Ablative Plating** — grants `Negates (Anti-Vehicle)` and `Negates (Anti-Armor)`. Narrower than a flat Armor increase on purpose: it specifically answers weapons built to kill vehicles, rather than making the model tougher against everything. Industrial materials science, not warded plate — the sci-fi register stays technological rather than borrowing anything from the Oath, since the faction using it first (Regiments) has no oath-access at all. *(First application: the Sable's standalone Ablative Plating option.)*
- **Warded Plate** *(name provisional)* — grants `Negates (Anti-Infantry)`. The infantry-scale cousin of `Ablative Plating`, and a direct payoff of the line above — Oathkeepers (Deep Oath) are the first faction with the actual oath-access to earn the "warded" version rather than the merely industrial one. *(First application: Oathkeepers' Terminator-tier Heavies, alongside `Shrug`.)*
- **Indomitable** — reduce the AP of incoming attacks by 1, minimum 0. Doesn't stop a dedicated anti-armor weapon from doing its job, but meaningfully blunts anything that wasn't built to punch through this specific armor. Deliberately not named `Bulwark` (already in use, and means Damage reduction, not AP reduction — a real naming collision caught before it shipped). *(First application: Oathkeepers' Heavies/Terminator-equivalent tier.)*
- **Crushing** — this weapon's Damage is increased by 1 against a target with Wounds 5+, and by 2 against a target with Wounds 10+. Deliberately named for what it does, not for any one weapon's fictional flavor, so it can be reused on future weapons that hit harder against heavy targets without being reskins of the same gravity-tech idea. The Wounds 10+ threshold isn't arbitrary — it lines up with the Armor-above-10 cascade threshold, so this trait reads as a direct answer to exactly the kind of target that rule exists for. *(First application: an Oathkeeper NCO sidearm option.)*
- **Shotgun** — this and `Meltdown` are **range-band-conditional**: their effect changes depending on which band the attack was fired from, rather than being a flat always-on modifier like every other trait above. At Close Range, re-roll all failed Attack Rolls. At Long Range, this weapon cannot be fired. Represents a close-range weapon that's devastatingly reliable up close and rapidly falls off past that — a hard cliff rather than a gentle taper. *(Rewritten for the Close/Effective/Long bands. The earlier "+2 Evasion at the outer band" penalty was a ±2 modifier, which the modifier policy now forbids; "cannot fire at Long Range" is the floor-style replacement and is a proposal — if the cliff should be softer, the alternative is a flat 5+ Attack Roll at Long Range.)* *(First application: the generic Scattergun weapon, D2; the Oathkeeper-exclusive `Oathkeeper Scattergun` variant runs D3.)*
- **Meltdown** — at Close Range, re-roll all failed Attack Rolls. If fired at Effective or Long Range instead, re-roll all **successful** Attack Rolls — a harsher penalty than Shotgun's, appropriate since Fusion-pattern weapons already sit in anti-armor territory and need a stronger reason not to just be fired from a safe distance. Applies to **every Fusion-pattern weapon in the roster retroactively** (Fusion Blaster, Heavy Fusion Blaster, and any future Fusion Pistol), not just new ones — the name is a deliberate near-homophone for Melta, the real-world-adjacent tech Fusion weapons are meant to evoke in this setting's fiction, the same naming trick as `HAMR`/hammer.
- **Impact (X)** — on a successful charge, roll X dice **per charging model** against the target unit's Armor, AP0, Damage 1 each. **Not an attack and doesn't use any weapon** — it resolves in total isolation, unaffected by weapon traits, Anti-[Keyword], or anything else that modifies an attack, because it represents the sheer physical weight of the charge and nothing else about the unit. Most effective against light/unarmored targets by design (AP0 means it never threatens real armor, only bulk-and-numbers). A genuine revival of the cut v0.3 `Impact(X)`, but a new shape, not a restoration — the old version is not what this is. Guideline rather than a hard Keyword lock: Infantry and Cavalry are the register this belongs to. X is driven by the individual model's own weight/violence of impact, not the unit's size — a jump-pack trooper might carry Impact (1), while something dropping from orbital height carries Impact (3), regardless of squad size either way.
- **Crushing Impact (X)** — the Vehicle/Monster register of `Impact (X)`, same structure and same isolation from weapons/traits. Currently stubbed at AP3/Damage 2 pending a real application — enough to threaten light armor or anything under Wounds 3, not enough to meaningfully touch another vehicle. *(First real application: Bastion — whether Vehicles get a standard melee profile at all, the way Infantry has universal Fists, or whether some vehicles rely on Crushing Impact alone with no ongoing melee option, is a genuinely open question, not yet decided either way.)*
- **Consumable (X)** — this weapon may only be used X times over the course of the game; once its uses are exhausted, it cannot fire again. Parallel notation to `Anti-[Keyword]`, `Deployment (X)`, and `Impact (X)` — a general-purpose way to describe limited-ammunition or one-shot weapons rather than inventing a bespoke rule per weapon. *(First application: Bastion's Hunter-Killer Missile, `Consumable (1)`.)*
- **Lance** — +1 AP on charge. The first trait priced under the new flat points formula: a flat +0.5, regardless of the weapon it's on. *(First application: the Heavy Ripsaw Sword, Repentia Squad — paired with `Onslaught` below, so charging turns a plain AP1 blade into effective AP2 with rerolled hits; off the charge it's just AP1.)*
- **Onslaught** — while charging, reroll failed hit rolls made with this weapon. A one-time reroll, not chainable against a second failure. Deliberately framed as the physics of impact (a charging body knocking the target's guard down for an instant) rather than personal fury, which keeps it distinct from the established "zealotry/fervor rerolls damage, not hits" convention (`Martyrs, all`, `Wrathbound`) — that rule is about anger sinking the blow deeper, this is about the shock of the charge itself, a different axis entirely. *(First application: the Heavy Ripsaw Sword, Repentia Squad.)*
- **Extra Hits** — when this weapon's Attack Roll is an unmodified 6, it generates one additional hit, resolved normally (including its own separate Wound Roll). *(No longer configurable — dropped its `(X)` threshold entirely; always keyed to a true Critical Hit, never a lower one like 7+ or 9+.)* Doesn't stack with other traits that also trigger off an unmodified 6, on the same Attack Roll — "doesn't stack" means they don't *compound*, not that they're mutually exclusive: if a weapon somehow carries both `Extra Hits` and a triggered-on-6 effect like `Anti-[Keyword]`'s free hit, a natural 6 triggers **both in full**, each resolving as its own separate instance, neither amplifying the other. *(First application: the Heavy Ripsaw Sword, Repentia Squad.)*
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
- **Aura of Discipline** *(Aura, 12")* — as an action, this model may make a Mettle check; on a pass, every friendly unit within 12" of it (including its own) discards all suppression markers. `Rallying Cry` widened from self-only to the aura — see §5 for the full reasoning.
- **Regeneration** — at the end of every round, regain 1d5 lost wounds.
- **Courage** — re-roll failed Mettle checks. *(Split out from the old Fearless, which used to bundle this with ignoring suppression markers — the two are more useful as separate, independently reusable pieces than as one combined trait.)*
- **Fearless** — ignores suppression markers on Mettle checks (the check is made as if the unit held none). No longer bundles Courage's re-roll — see above.
- **Entrenched** — while in cover, +1 Armor and gains `Courage`.
- **Camouflaged** — +1 Evasion while in cover.
- **All-Terrain** — ignores difficult terrain penalties.
- **Shrug (X)** — for every wound this model would suffer, roll a d10 and ignore that wound on an X or better (the universal floor/ceiling applies: an unmodified 1 always fails, an unmodified 10 always succeeds). The system's version of an invulnerable save — deliberately rare by design intent, reserved for specific named wargear rather than a unit-wide rule, so it stays a genuine event rather than a roll made on every single hit across the whole army. *(First intended application: a Storm Shield-equivalent Oathkeeper wargear option, possibly also an Iron Halo-equivalent for Oathmaster — neither built yet.)*
- **Undaunted (X)** — when this unit fails a Mettle check that would step it down its morale track, it may immediately attempt one additional, unmodified roll against a fixed target number of X; on success, it does not step down. Mechanically `Shrug`'s own shape — a flat second roll against a static threshold, not modified by the model's own stats — retargeted at morale instead of damage. Kept as its own name rather than overloading `Shrug`, since two different effects can't share one trait name (the same rule that separated `Bulwark` from `Indomitable`). *(First application: Repentia Squad, at `Undaunted (7+)`, gated on a Repentia Superior being present in the unit — kill her, and it stops working for whoever's left.)*

**Movement**
- **Flying** — ignores models and terrain while moving. Now a standalone entry rather than an Aerial-exclusive bundle: anything can be granted it. The Aerial keyword is conventionally paired with it alongside `Soaring Above`, which is what actually distinguishes a real aircraft from anything else that merely ignores terrain.
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
4. **Resolved by the Platoon/CORE rewrite (§8):** there's no longer a generic ARMOR/SUPPORT ability to leave undesigned — every Platoon bonus is faction-specific from the start. What's actually open now: every faction's Platoon bonuses are undesigned except Regiments' Infantry Platoon (`Massed Ranks`). This also **retires the five old per-faction "Doctrines"** (`Fix Bayonets`, `Sealed Orders`, `Hold the Oath`, `Act of Faith`, `Break the Chains`) — they were the same once-per-game, rest-of-round shape the generic Platoon Abilities used, and that shape is gone. They need redesigning as CORE bonuses, not transcribing as-is (see item 10 below).
5. **Platoon slot constraints aren't encoded in the `.gst`** — the proposed spread in §8 is documented but not enforced by the force entry itself.
6. ~~The AFV's cost is 2.4 rifle squads. If centrepieces feel over-taxed, soften `SIZE_EXPONENT` from 0.85 toward 0.90 in `points.py`.~~ **Stale mechanism, not yet re-evaluated under the new formula.** `SIZE_EXPONENT` no longer exists — Step 4's sublinear Size Factor was retired outright in the points rebuild (§11 Step 4). Under the rebuilt formula, the re-priced AFV (238pts, treated as Regiments' MBT in the Phase 3 watered-down slice) sits at ~2.2× the re-priced Rifle Squad (106pts) — a similar ratio by coincidence, not because the old lever survived. If centrepieces still feel over- or under-taxed once played, the levers now are Armor/Wounds/Speed's own factor curves or the currency scale, not a size discount.
7. ~~No mission or scenario has been written against the current rules.~~ **Resolved (2026-09-28):** "Claim the Ground," §9 — one working mission, not the full planned 5–10, but enough to actually play.
8. ~~No general facing/LOS section.~~ **Resolved (2026-09-28):** §6's new Facing & Arcs subsection — covers ordinary play, deliberately doesn't chase every corner case.
9. ~~The toolchain is duplicated across the `Praxis Belli` project workspace and the `PraxisBelli` git repo.~~ **Resolved (2026-09-28):** the repo now lives at `C:\Toolbox\ToolboxVault\PraxisBelli`, and `Documents\NewRecruit\data\PraxisBelli` is a Windows junction pointing at it — one real copy, no drift risk left.
10. **`PraxisBelli.gst` is missing roughly 30 rules that already exist in this glossary and in faction-identity.md.** The user is keeping the `.gst` as-is and rebuilding the three `.cat` rosters from scratch by hand rather than resetting everything — this list is what still needs transcribing into the `.gst` at some point during that rebuild (definitions live at their linked source, not repeated here, to avoid a third copy going stale):
    - **Weapon/unit traits** (full text in this document's glossary, §"Weapon & unit trait glossary" above): `Bombardment`, `Traversing`, `Ablative Plating`, `Indomitable`, `Crushing`, `Shotgun`, `Meltdown`, `Impact (X)`, `Crushing Impact (X)`, `Consumable (X)`, `Conscript`, `Critical Weakspot`, `Fixed`, `Combat Medic`, `Courage`, `Shrug (X)`, `Jump Jets`, `Deployment (Scout)`, `Deployment (Infiltrate)`, `Picket`, `Barrage`. **Transcribe the current text** for `Anti-[Keyword]` and `Extra Hits` specifically — both changed shape this pass (Round 3) and no longer match what an earlier draft of this list might have assumed.
    - **Faction signature traits** (full text in faction-identity.md, per-faction "Signature trait —" entries): `Bound Spirit` (Forgesworn), `Oathbound` (Oathkeepers), `Martyrs, all` (Saints), `Wrathbound` (Wrathful Oathbreakers). *(`Massed Ranks` no longer belongs on this list — it's now Regiments' Infantry Platoon's CORE bonus, not a faction-wide signature trait; see §8. Regiments needs a new signature trait before this list is complete again.)*
    - **Platoon Doctrines, retired — do not transcribe as-is.** `Fix Bayonets`, `Sealed Orders`, `Hold the Oath`, `Act of Faith`, `Break the Chains` are all superseded by the Platoon/CORE rewrite (item 4 above); each faction needs a redesigned CORE bonus instead.
    - **One not-yet-in-glossary trait**: `Warded Plate` (faction-identity.md, Oathkeepers' Heavies/Terminator family section) — name still provisional.
    - **Present in the `.gst` but with stale text needing a rewrite, not an addition**: `Fearless` (likely still the old bundled version), `Entrenched` (likely still says "reroll failed Mettle checks" instead of granting `Courage`), `Optics` (likely still the old priced-at-0 stub text), `Anti-` (still the old ×2-hits version — the whole mechanic changed, not just the wording).
11. **The v0.5 redesign, status as of this pass:** §3, §5 (Mettle-check formula plus the new Damage Track), §7 (Role/Keyword), §8 (Platoon/CORE), and — as of a full from-scratch rebuild — §11's core points formula (Model Cost, Weapon Cost, `Anti-[Keyword]`, weapon-trait and named-ability tiers, `Transport(X)`) are all converted and written into the sections above, plus a new Size stat (Reference — Unit Profile; §10). **Still not applied:** §4's own `Fists`→`CCW` prose rewrite (the decision itself — 0 points, fixed — is made), exhaustive classification of every remaining trait/ability against the new tiers (only a first pass exists), the four faction signature-trait multipliers, the range multiplier (flagged as never re-derived, not just unconverted), and the standard game's point target (1000 vs. 2000 vs. 3000, still open — independent of the formula itself, which prices per-unit regardless of the total). **Actually re-costing the roster has started, narrowly.** `points.py` itself was rebuilt to match this section (2026-09-28) and verified against the Rifle Squad anchor by hand. A watered-down slice of Imperial Regiments — Rifle Squad, Veteran Squad, Scout Element, Armored Personnel Carrier, Armored Fighting Vehicle (path-to-playtest-2026-09-28.md Phase 3, "just enough to see the system in motion") — was re-priced 2026-09-29 in `factions/imperial_regiments.json` (each unit carries its own `_v05_note` explaining what changed) and regenerated into `Imperial Regiments.cat` via `build_cat.py`, which needed its own fix in the same pass (it was reading a `toughness` characteristic the `.gst` had already renamed to `Wounds`, and was silently crashing on any rebuild). The rest of that faction (Regimental Officer, Conscript Mob, Storm Squad, Heavy Weapons Team, Field Gun Battery, Tank Destroyer) and every other faction/unit stat line remain stale d10-era numbers until their own pass happens. A handful of pure d10-era notation leftovers outside the attack/Mettle engine (`Dangerous` terrain's d10 roll, `Blast`'s 1d5"/1d10" scatter, `Regeneration`/`Combat Medic`'s 1d5, `Shrug (X)`'s d10, `Critical Weakspot`'s unmodified-10, `Undaunted (X)`'s "impossible on a d6" gap) are also untouched — a separate, smaller cleanup pass.
12. **Standing policy, confirmed 2026-09-28: individual stat-line/Evasion-template conflicts across `faction-identity.md` are expected and not worth flagging one at a time anymore.** No current stat line on any built unit can be trusted until the benchmark/points rebuild (item 11 above) actually lands — every conflict between an existing stat and a new rule (the Evasion archetype template, the Armor cascade, the AP scale) is a symptom of the same not-yet-done rebuild, not a separate decision each time. Surface a conflict only if it changes a *mechanic* (like the Oathkeeper Armor↔Evasion trade lever disappearing did); pure number mismatches wait for the rebuild.
