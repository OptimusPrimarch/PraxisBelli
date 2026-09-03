# Praxis Belli — Design Bible

**Status:** v0.4 — mechanics and formula are authored here (and in `reference.html`, its formatted twin).

**Source of truth — two modes, not one:** while actively building or revising stats and profiles together, this document and `points.py`/`factions/*.json` lead — that's what a design session *is*. Outside of that, **NewRecruit is the default source of truth**: `PraxisBelli.gst` and the `.cat` files in `C:\Users\darry\Documents\NewRecruit\data\PraxisBelli\` reflect whatever was last hand-edited there directly, which may not match what's written here. When the two disagree, that's a conflict to surface and resolve, not something to silently overwrite in either direction. The older `Documents\NewRecruit\data\Praxis Belli\` folder (with a space) is superseded regardless of either mode; it holds an earlier `Praxis Belli.gst` plus Oathbreaker Legions / Oathkeeper Cohorts catalogues on a different game system ID.

**Design lineage:** *Marcher: EAW* (Platoon frame, Transports, attacker-rolled Evasion/Armor), *Ravaged Star* (d10 roll-over engine, 1-fails/10-succeeds, the Damage stat, "Shaken"), and *Warmachine MkIV* (facings and arcs, model-count transports).

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

- **Mettle is additive and higher-is-better** — `d10 + Mettle ≥ 10 + suppression markers`. Every stat on the card now reads "bigger is better."
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

**Every check is roll-over on a d10: meet or exceed the target number to succeed.**

**Dice floor/ceiling, universal:** an unmodified **1 always fails**; an unmodified **10 always succeeds**.

### The attack sequence

1. **To-hit** — roll d10 per attack die against the target's **Evasion**. Total dice = weapon's Attacks × models firing.
2. **Damage check** — each hit rolls again against the target's **Armor**, after **AP** is subtracted. Each success inflicts the weapon's **Damage** value in wounds against the target's **Toughness**.

Higher Evasion = harder to hit. Higher Armor = harder to damage.

There is no attacker-side accuracy stat. To-hit difficulty is entirely defender-side; attacker differentiation comes from traits, rerolls, and Anti-[Keyword] weapons.

### Armor above 10

Armor is **not capped at 10**. When a target's Armor after AP exceeds 10, an unmodified 10 no longer succeeds automatically — instead it buys a **second roll** against `Armor − 10`, cascading again if that also exceeds 10.

A hull at Armor 17 struck by an AP 0 weapon needs a 10, then a 7+: a **4% chance**. Vanishingly unlikely, never impossible, and the curve continues smoothly instead of hitting a wall.

This makes **AP the only real answer to heavy armor**, which is exactly right. That same Armor 17 hull struck at AP 6 is rolling against an effective 11 — more than twice as likely to take a wound.

*(Borrowed from Marcher, which likewise permits Armor beyond the die.)*

### The AP scale

AP is calibrated against real anti-armor performance, so weapon design has an intuitive reference:

| AP | Reference | | AP | Reference |
|---|---|---|---|---|
| **0** | Modern assault rifle | | **4** | 57mm |
| **1** | Magnum rifle cartridge | | **5** | 76mm |
| **2** | 20mm autocannon | | **6** | 88mm |
| **3** | WWII 37mm | | **7** | Modern 120mm sabot |
| | | | **8** | Railgun |

**Most infantry weapons sit at AP 0.** Penetration is bought through heavy weapon teams and vehicles, not carried by line infantry — a large part of why combined arms is mandatory rather than merely encouraged.

### Range bands

Range is a single Short value on the profile. Medium = 2× at +1 to the target's Evasion; Long = 3× at +3. **Accurate** ignores all range penalties.

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
Roll d10 + Mettle.  Pass if the total ≥ 10 + suppression markers held.
```

Higher Mettle is better, like every other stat on the card. A unit with Mettle 4 holding two markers needs an 8+.

- **Pass** — remove **one** suppression marker.
- **Fail** — step **up** one level on the track.

**Check timing:** at the start of a unit's activation if it holds any markers, or immediately when an effect forces one.

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
| **Impassable** | Ground units cannot move through at all. |

A ruin is `Obscuring + Cover + Difficult + Blocking`. A sandbag line is `Obscuring + Cover`. A minefield is `Dangerous`.

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

> **Note:** `Impact(X)` and `Fear` from earlier drafts are **gone**. Cavalry's charge bonus is now **Run Them Through**, and the Monster signature is **Terrifying**.

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

- **3 or more** carry `Difficult` or `Impassable` — ground armor cannot cross freely
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
| Major bonus | **1.30** | Linked-Weapon, Blast (L), Engulf (L), Guided, Indirect, Overcharge |
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
- **Guided** — if the target is visible to an allied RECON unit, decrease the target's Evasion by 3, disregarding all other modifiers.
- **Accurate** — ignore all range penalties.
- **Optics** *(rules stub)* — "helps land hits"; mechanism not yet written. Costs nothing in the points formula until it is. Do not treat a weapon carrying it as finalized.

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
- **Overcharge** — this weapon may fire in Overcharged mode: its AP and Damage are each increased by 2 for that attack. For each unmodified roll of 1 made for this weapon's attack, the bearer suffers a Damage 1 hit that cannot be saved against, in addition to any other effect of that roll.
- **Anti-[Keyword]** — against a target with the matching keyword, each successful damage roll counts as two hits instead of one; because hits are allocated individually, the excess may spill onto other models in the unit. Defined for: Aerial, Armor, Cavalry, Command, Infantry, Line, Monster, Recon, Shock, Support, Towable, Vehicle.
- **Bulwark** — reduce incoming damage by 1, to a minimum of 1.
- **Ablative Plating** — while this model would take doubled damage from a hit with the `Anti-Vehicle` or `Anti-Armor` trait, it instead takes that damage normally. Narrower than a flat Armor increase on purpose: it specifically answers weapons built to kill vehicles, rather than making the model tougher against everything. Industrial materials science, not warded plate — the sci-fi register stays technological rather than borrowing anything from the Oath, since the faction using it first (Regiments) has no oath-access at all. *(First application: the Sable's standalone Ablative Plating option.)*

**Cost-modifying traits**
- **Conscript** — this unit costs **25% less**. It may never re-roll a die for any reason, and may not take the Rally action. *Conscripts get raw numbers and none of the benefits of training: `Entrenched`'s Mettle re-roll and `Massed Ranks`' to-hit re-roll both go dead, and once suppressed they can only clear markers one at a time by passing checks they are bad at.*
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

**Movement**
- **Scout Move** — after deployment, before the first activation of the game, this unit may make a free move up to its Speed. *(First application: the Weasel — the one vehicle in the roster whose entire job is getting somewhere before the shooting starts.)*

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
3. **`Optics` (Marksman Rifle) is a rules stub** — "helps land hits," no mechanism defined, priced at 0 until it is.
4. **ARMOR and SUPPORT generic Platoon Abilities** are undesigned (the five faction-specific doctrines exist; the three generic Vanguard-Platoon abilities from §8 are Line/Shock/Recon only).
5. **Platoon slot constraints aren't encoded in the `.gst`** — the proposed spread in §8 is documented but not enforced by the force entry itself.
6. **The AFV's cost is 2.4 rifle squads.** If centrepieces feel over-taxed, soften `SIZE_EXPONENT` from 0.85 toward 0.90 in `points.py`.
7. **No mission or scenario** has been written against the current rules.
8. **No general facing/LOS section** — `Armored Front` and the arc traits imply one exists, but it isn't written.
9. **The toolchain is duplicated** across the `Praxis Belli` project workspace and the `PraxisBelli` git repo (copied, not moved) — a real drift risk until one is picked as canonical.
