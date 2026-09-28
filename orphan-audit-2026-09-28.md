# Praxis Belli — Orphan Audit & Rebuild-vs-Overhaul Evaluation

*2026-09-28. Read-only pass: nothing in the design docs, `.gst`, `.cat`, or tooling was edited. This file is the only thing written.*

**Scope.** Non-legacy documents: `design-bible.md`, `faction-identity.md`, `reference.html`, `ProjectSummary.md`. Game/catalogue side: `PraxisBelli.gst`, the four `.cat` files in `Documents\NewRecruit\data\PraxisBelli\`, plus the tooling that feeds them (`points.py`, `build_cat.py`, `factions/imperial_regiments.json`). `*_legacy.*` files ignored except as diff baselines.

**Tags used below.** **[QUEUED]** = already listed in the bible's v0.5 Decision Queue (I don't re-explain it). **[NEW]** = found in this pass, not in the queue. **[DRIFT]** = was already out of sync before the v0.5 changes.

---

## 1. Bottom line

**Overhaul the design layer. Rebuild the numbers layer from scratch. Do not start the whole project over.**

- The opening ~15% of `faction-identity.md` (cosmology, First Binding, xenos, proxy contract) has **no mechanical dependency** on any v0.5 change. The faction/vehicle/roster sections that make up most of the rest are *shape-first* prose (packages, identities, real-world anchors). By line count, only ~43 of its ~730 lines mention TYPE/CATEGORY/Role names and ~48 carry AP/Armor/Evasion numerics, and nearly all numbers are already flagged "open." That's the expensive design capital, and it survives.
- Almost everything **numeric** is dead: every AP/Armor/Evasion/Mettle value, every points cost, `points.py`'s probability core, the whole `factions/` JSON, and the Regiments `.cat`. None of that is worth patching, because it can't be patched one value at a time. Each number must be re-derived from the new formula.
- Two things are closer to *new writes than edits*: bible **§7, §8, §11** (Role/Keyword, Formations, points) and `reference.html`.
- **Cost is dominated by unmade decisions, not typing.** Roughly seven open questions (§5) gate most of the mechanical work. Answer those first, then the rest is largely mechanical.

---

## 2. Orphan catalogue — documents

### A. Role + Keywords replace TYPE/CATEGORY

The queue says what gets rewritten (§7, §8, §10, glossary). These are the *dependents* it doesn't mention.

| # | Orphan | Where | Tag |
|---|---|---|---|
| A1 | **Evasion is "templated by TYPE"** — but TYPE is being deleted. The template rows (Heavy Vehicle / Light Vehicle / Infantry / Elite) have nothing to key on unless they become keywords, and keywords "do nothing on their own." | bible §3, lines 106–119 | NEW |
| A2 | **Objective rules are keyed on TYPE** (Infantry/Cavalry/Towable claim; Vehicle/Monster/Aerial contest only). Under "keywords do nothing on their own," the load-bearing combined-arms rule (§9.1) has no home. It needs a trait or an explicit core rule that reads a keyword. | bible §9.1, lines 329–336; also `Boots on the Ground` (LINE) | NEW |
| A3 | **`Guided` / `Spotter` / `Indirect` require "an allied RECON unit."** If RECON is a Role (grants nothing, per the queue), the sentence is dangling. Is RECON also a Keyword? Same question for every `Anti-Line/Armor/Support/Shock/Command/Recon`. | bible glossary 582–588, 606; .gst `Guided`, `Spotter` | NEW |
| A4 | **Dedicated Transports "take the CATEGORY of the unit they carry"** — the entire slot-neutrality argument and the `Anti-Line` vs `Anti-Armor` "two threat profiles" argument ride on category being both a slot *and* a target. .gst `Transport:` says the transport "gains all the category keywords of embarked units." | bible §10, 373–382; .gst | QUEUED (partly) |
| A5 | **Hull-class doctrine table** (Bus / Gunboat / Assault Transport per faction) depends on A4's inheritance rule. | faction-identity 223–235 | NEW |
| A6 | **Hard category caps table** (per-faction COMMAND/LINE/RECON/… min–max) becomes Role caps; Saints' "COMMAND 1–2" and the "each faction has exactly one category it can push further" paragraph go with it. Also superseded by CORE's "that Role's slot cap is raised." | faction-identity 198–213 | NEW |
| A7 | **"Design tool: change a unit's CATEGORY and it costs you the benefits"** is gone. Role grants nothing, so a Role change costs nothing. Concretely orphaned: **Mink's** whole design beat ("loses the benefits of recon — no stat compensation, just narrower"), **Fisher "flips CATEGORY to ARMOR"**, Marten Forward Observer's "Spotter *without* RECON, stays SUPPORT," Oathkeeper Paragons LINE-despite-elite, Oathguard "SUPPORT only" reasoning. These can be *re-expressed* (Weasel/Stoat now *pay* for Spotter/Camouflaged/All-Terrain as traits; Mink simply doesn't have them), but the current prose describes a mechanism that no longer exists. | faction-identity 299–301, 337, 418, 539, 542 | NEW |
| A8 | **"Every Vehicle ignores Heavy via its TYPE" (Hardpoints)** appears as a blanket rule in the Sable note, the Tayra section, and `Bombardment`'s glossary text ("the first unit to deviate from the blanket rule"). After the change, Hardpoints is an assigned, priced trait; Tayra simply doesn't take it. The "deviation" framing is void. | faction-identity 331, 383; bible 593 | NEW |
| A9 | **Monster-TYPE reasoning for Fanatic Mindless / Ascendant Warsuits.** Argument was: "cover-benefit defines Infantry TYPE; Mindless strips cover; therefore Monster; Monster grants `Terrifying` free." All three links break. Entrenched (the cover benefit) and Terrifying become individually assigned traits. These units now have to *buy* Terrifying, and the "Infantry vs Monster" split needs a new reason (or none). | faction-identity 606, 626, 180 | NEW |
| A10 | **`Anti-[Keyword]` count:** queue says "fixed 12-label list"; bible glossary lists 13 (Aerial, Armor, Caster, Cavalry, Command, Infantry, Line, Monster, Recon, Shock, Support, Towable, Vehicle). Trivial, but the queue's premise is off by one. | bible 606 vs queue item 1 | NEW |
| A11 | **`Caster`** is already a standalone Keyword "independent of TYPE and CATEGORY" — it's the one thing that *already matches* the new model. Fine as-is. | bible 605 | — |
| A12 | **17 rules currently bundled via TYPE/CATEGORY must be individually assigned and priced:** Bulwark, Hardpoints, Inspiring/Leadership Aura, Boots on the Ground, Spotter, Camouflaged, All-Terrain, Brutal Assault, Where We're Needed, Entrenched, Run Them Through, Armored Front, Terrifying, Flying, Soaring Above, Trailer, Emplaced Weapon. Text mostly survives; `Inspiring Leadership` and `Entrenched` need real rewrites. | .gst categoryEntries; bible §7 | QUEUED |

### B. d6 conversion and scale knock-ons

The queue's item 6 lists nine d10 leftovers. **What it doesn't list** (all [NEW] unless noted):

| # | Orphan | Where |
|---|---|---|
| B1 | **Principle 0's anchor squad is Evasion 6 / Armor 4**, and §11 says "Baselines are Evasion 6." The new Evasion table calls **Evasion 5 "Infantry baseline"** and Evasion 6 "elite / dedicated dodge specialists." The unit-of-account contradicts the template. | bible 46 vs 108–116, 439 |
| B2 | **Evasion 7+ as a base value is now illegal** ("reachable only through modifier stacking"). Storm Squad and Scout Element (Eva7), Fanatical Sisters (Eva7) violate it in the `.cat`. | bible 117; Regiments/Saints .cat |
| B3 | **Light Chassis is Eva6** ("trades armor for speed and *visibility*"). Template says Light Vehicle = Eva 3–4. Direct conflict with the family's stated identity. Medium (Eva5) falls in a gap the template doesn't cover. | faction-identity 252–253, 416 |
| B4 | **Oathkeepers' Armor↔Evasion 1:1 trade ladder** and **Saints' "+Armor with no Evasion cost, Mettle is the lever"** are design levers that no longer exist — Evasion is templated and "veterancy no longer differentiates through Evasion." Oathkeeper infantry at Eva 3–4 also sit outside the Infantry=5 template. | faction-identity 177, 481–491 |
| B5 | **Armor cascade now starts at 7, not 11.** The prose treating cascade as exotic is inverted: "Armor 10 sits exactly at the pre-cascade ceiling," "Bolt-on Armor makes Wolverine the *first* unit able to reach the cascade," "Bastion Arm14 well past the threshold," "obliterator rule of thumb." On d6, the Regiments AFV (7) and Tank Destroyer (8) *already* resolve to the same 13.9% at AP0, and Arm 6/7/8 barely differ. | faction-identity 447, 461, 553, 692; bible 122–127 |
| B6 | **Every ±1 is now worth ~1.7× more** (a d10 step is 10%; a d6 step is 16.7%). This silently re-weights every small design lever: Bolt-on Armor +1/+2 ("deliberately small"), Camo Netting/Camouflaged/Obscuring +1 Eva, Cover +1 Armor, Entrenched +1 Armor, Shaken −1/−1, Sworn Protectors +1 Armor, NCO +1 Mettle. | throughout |
| B7 | **Stack audit needed for ±1 sources.** Cover tag (+1 Armor) + `Entrenched` (.gst: "an *additional* +1 ARM") = +2, which trips the queue's own item 5 (≥2 modifiers should be floors). Same shape: Obscuring (+1 Eva) + Camouflaged + Camo Netting (+1, "stacks with Obscuring's own +1"). | bible 235–236, 274; .gst `Entrenched`; faction-identity 407 |
| B8 | **Item 5 (modifier policy) hits traits the queue didn't name:** `Overcharge` (+2 AP, +2 Dmg — *2 of a 5-step AP scale*), `Shotgun` (+2 Evasion), `Spearhead`'s +2 AP, .gst `Lance` (+2 AP), `Break the Chains` (+2 Speed is fine; it's inches). | bible 604, 612; 303 |
| B9 | **AP compressed to 0–4, but the roster is built on 0–8.** Existing AP≥5 weapons: ATGM (5), Heavy ATGM (7), Laser Cannon (6–7), Main Cannon (5), Battle Cannon (5), Prosecution Cannon (7), Heavy Fusion Blaster (8), **infantry** Fusion Blaster (8 in Saints `.cat`), Plasma Sword (4 = the new ceiling). Wolverine's Heavy Laser Annihilator has no numbers yet but is meant to top the roster. The Weapon Identity tier table (Special AP4+, Obliterator AP7+, Ordnance AP4–6) is unreachable. Whether AP is rescaled or anti-armor moves to `Anti-Armor`/Damage is a *design decision*, not arithmetic. | faction-identity 615–617, 688–690; both `.cat` |
| B10 | **`Accurate` "ignores all range modifiers"** — under the new bands that includes losing the **+1 close-range bonus**, which is almost certainly unintended. Should read "ignores the −1 at long range." | bible 149, 586 |
| B11 | **Range bands changed structure** (old Short/Medium/Long with 2×/3× → +1 / +0 / −1 on half-range). Still using the old language: `Shotgun` ("within Short range… outer band"), `Meltdown` ("Short… Medium or Long"), Oathkeeper Scattergun ("Short 9", max 18"), and the `.cat` `Range` field values (`M`, `ST`, `LT`). | bible 612–613; faction-identity 517; .cat |
| B12 | **`Crushing`'s rationale is orphaned:** "the Toughness 10+ threshold lines up with the Armor-above-10 cascade threshold." Cascade is now 6. (Note the `.gst` `Crushing` is Armor-based, 6+/8+/10+ — which accidentally fits d6 better than the doc's Toughness version. [DRIFT]) | bible 611; .gst |
| B13 | **`Critical Hit` = natural 6 = also plain success.** `Extra Hits (X)` default 10 and `Critical (X)` default 10 are unreachable [QUEUED], but note the consequence: Fanatical Sisters' Heavy Ripsaw (`Extra Hits (10)`), Defensors' Halberd (`Extra Hits (10)`), Ascendant Ripsaw (`Extra Hits (9+)`), `Critical (10)`, `Critical (10+)` all need a real threshold. On d6 the only reachable non-trivial thresholds are 5+ and 6. | faction-identity 585, 599, 608, 615, 630 |
| B14 | **Bastion "Eva1 = redundant with Eva2" (90%/90%)** — reasoning holds structurally on d6 but the numbers are d10; Eva2 is now 83%. | faction-identity 553 |
| B15 | **§9.3 "Damage ≥ 6 vs Toughness 10 chassis"** is stale against Toughness 14–18 (Heavy/Bastion). Faction-identity already updated its version of the rule; the bible didn't. [DRIFT] | bible 349 vs faction-identity 692 |
| B16 | **Mettle range: values 6–7 (Oathkeepers, Commander Met7) now saturate.** `d6 + Mettle ≥ 6 + markers` means Met 7 passes with no roll until 2+ markers. [QUEUED as "recalibrate," but the *consequence* for Oathbound's "auto-passes first Mettle check" and `Fearless`/`Courage` stacking isn't noted — those become redundant on high-Mettle units.] | bible 174–177; faction-identity 165, 575 |

### C. Morale redesign

| # | Orphan | Where | Tag |
|---|---|---|---|
| C1 | **Bible's own §5 track table still says Shaken = "a worsened Mettle."** The queue item cuts it; §5 wasn't updated (only the formula line was). Internal contradiction inside one document. | bible 220 vs queue item 2 | QUEUED (visible) |
| C2 | **Platoon Ability `Hold Fast`** ("suppression markers do not worsen Mettle checks") describes the *old* Mettle-worsening model and is referenced from §5's marker-removal table. | bible 196, 302 | NEW |
| C3 | **Doctrines built on the old morale track:** `Fix Bayonets` (ignore Frozen), `Hold the Oath` (ignore Suppressing), `Act of Faith` (auto-pass Mettle checks, wound at end of round), `Break the Chains` (auto-fail next Mettle check). Also superseded wholesale by D1. | faction-identity 150, 168, 179, 194 | NEW |
| C4 | **Existing `Rallying Cry`, `Aura of Courage`, `Leadership Aura` ("use this model's Mettle")** overlap with the new **Leader trait** (strips markers from own/aura unit). `Bound Spirit`'s trade-off text ("offset by losing Leadership Aura") re-points at whatever replaces it. | faction-identity 156, 580, 667; .gst | NEW |
| C5 | **"Rare, expensive, faction-signature" immunity traits — but they're currently faction-wide baseline for whole factions:** Oathbound gives *every* Oathkeeper `Courage`+`Fearless`; Wrathful Marine units get `Fearless`; Bound Spirit is total immunity; Fanatical Sisters stack `Negates (Suppressing)`+`Undaunted`+`Terrifying`. Consistent with "signature," but the ×1.10–1.15 faction multipliers were guesses sized for the *old* commonness of these traits. Reprice is queued; the *scale of exposure* isn't noted. | faction-identity 165, 189, 588; 664–672 | QUEUED (partly) |
| C6 | **`Terrifying` = "Mettle check" in the bible, "morale tests" in the .gst.** These are now *defined as different things* (§5 naming note). The mismatch matters: Mindless/Undaunted only touch Morale tests, so Terrifying's outcome vs. Mindless units differs by which text is right. | bible 184, 277; .gst `Terrifying` | DRIFT |

### D. Formations / CORE

| # | Orphan | Where | Tag |
|---|---|---|---|
| D1 | **All bespoke Platoon Abilities:** `Hold Fast`, `Break the Line`, `Fast as the Wind`, the two undesigned (ARMOR/SUPPORT), **and all five faction Doctrines** (`Fix Bayonets`, `Sealed Orders`, `Hold the Oath`, `Act of Faith`, `Break the Chains`). One uniform template replaces them. | bible 300–306; faction-identity 150, 159, 168, 179, 194 | QUEUED |
| D2 | **Open Thread #4, #5 and "Systems still owed" bullets 1–2** (undesigned ARMOR/SUPPORT abilities; slot caps not encoded) are void or reframed by CORE. | bible 685–686; faction-identity 717–719 | NEW |
| D3 | **"Once-per-game, rest-of-round" ability shape** is replaced by a permanent passive. Anything referring to "a once-per-game Platoon Ability" (incl. the Command-Points rejection note: "extend Platoon Abilities instead") loses its extension point. | bible 300; faction-identity 285 | NEW |
| D4 | **Terminology split:** bible says "Platoon" throughout (§8, §9, §10, §11 target scale); queue and `.cat` force entries say "Formation" ("Vanguard Formation," "Standard Force"). Army scaling ("1 Platoon per 500 pts, min 1 per 1000") vs "1000 pts / 2 Platoons" §11 — and the queue floats a 3000-pt game. | bible 287, 319, 410 | NEW |
| D5 | **Embedded units "change the host's CATEGORY"** (Embedded Leader → LINE; Embedded HWT → LINE) so it doesn't consume its own slot. Depends on Role being mutable at list-building — plausible under Role/CORE, but rewrite required. | bible 308–315 | NEW |

### E. Points formula / `CCW`

| # | Orphan | Where | Tag |
|---|---|---|---|
| E1 | Whole formula is d10-derived: `P_soft`, `P_hard`, Evasion/Armor factor tables, "Cap Evasion at 9," Armor rows 10/11+, `BASE_MODEL`/`BASE_WEAPON`. | bible §11; `points.py` | QUEUED |
| E2 | **Every documented price** (chassis and weapon costs quoted inline in the Saints/Regiments prose, e.g. "Prophesier MBT 240," "Fanatic 23 pts," "Commander 96") is a d10 output. | faction-identity 573–634 | NEW (scale) |
| E3 | **`Fists` → `CCW` knock-ons:** the `Unarmed` trait (Fists' +1 Eva/Armor to the target) has no stated fate; the "69% of a Bayonet" figure; the **`Fixed` trait's canonical example is "a Bayonet on a Rifle"** — but the new anchor has *no default bayonets*. Regiments' `.cat` Rifle Squad has a Bayonet `Fixed`; Saints baseline is "chassis+knife+rifle." What does `Fixed` still protect? | bible 157–167, 627 | QUEUED (partial) |
| E4 | **"Rifles *and bayonets*" appears as the anchor definition** in §11 "The currency scale" and the README; queue says rifles + CCW only. | bible 535; README | NEW |
| E5 | **80/20 model/weapon split** (currently ~62/38 on the anchor per `points.py`'s `BASE_MODEL` 6.20 × 10 models) means every existing *relative* statement about weapon cost is off — e.g. "HMG is the most expensive infantry weapon," the Elite Constraint doctrine ("priced better weapons per model" as compensation gets *cheaper*, which strengthens it, but the doc argues from the old ratio). | bible 461; faction-identity 123–139 | NEW |
| E6 | **Traits that used to be free bundles need tiers**; the Major/Minor flat tiers (15/5 pts) are sized for a 100-pt rifle squad on the *old* curve. Item 1 items (Bulwark, Hardpoints, Spotter, …) each need placement. | bible §11 Step 5 | QUEUED |

### F. Pre-existing dangling references [DRIFT]

None of these are caused by v0.5, but they'll surface during any sweep and are cheap to fix together:

- **`Priority Orders`, `Blood Surge`, `Leadership Abilities`** appear in §11 Step 5 and are defined **nowhere** in any current doc. (`Blood Surge` was `Blood Debt`'s ability; `Blood Debt` retired.)
- **Bible §"Roster — Imperial Regiments"** says Levy/Fusilier/Grenadier/Vanguard/Ranger/Ballistier/Officer are "**fully built**." Neither `factions/imperial_regiments.json` nor `Imperial Regiments.cat` contains them. Both still hold the *old* names (Conscript Mob, Rifle Squad, Veteran Squad, Storm Squad, Scout Element, Heavy Weapons Team, Field Gun Battery, APC, AFV, Tank Destroyer, Regimental Officer). The **entire Mustelidae vehicle roster and Wolverine/Badger exist only as prose.** §11's validation table also uses old names.
- **Open Thread #9** ("toolchain duplicated across `Praxis Belli` workspace and `PraxisBelli` git repo") is outdated; the duplication is now **vault vs. `Documents\NewRecruit\...`**. The NewRecruit folder holds `design-bible.md` (byte-identical to `design-bible_legacy.md`), and `faction-identity.md` / `reference.html` (identical to the vault's). Risk: editing the wrong copy. README there still says d10, "Saints = stub," "Wolverine deliberately not part of the family."
- **Bible §11 constants disagree with `points.py`:** bible says `5.83 × …` (model), `6.67 × …` (weapon), Transport `× 0.417`; `points.py` has `BASE_MODEL = 6.20`, `BASE_WEAPON = 7.09`, Transport `× 0.439`. Bible also says a plain grunt costs "7 points" (5.83 would give 5.83). `points.py`'s own header comments still carry the d10 AP scale (0–8) and "rifles and bayonets." One of the two is stale even before the d6 rebuild.
- **`Barrage`**: glossary defines it as a "Morale test on hit" trait; faction-identity (line ~149) also describes an unbuilt "Barrage artillery trait — fire without LOS." Two different concepts, one name.

### G. `ProjectSummary.md`

Says **"Iron Horizon,"** 2000-pt game in ~2 hrs, "first leadership check," and a "unit-building matrix" goal. The bible says Praxis Belli, 1000-pt standard, no leadership check. Bible's own housekeeping note already flags it; please confirm whether "Iron Horizon" is a dead name or a distinct project.

### H. `reference.html`

**Byte-identical to `reference_legacy.html`** (176 KB, 15 sections). It is a complete d10 / TYPE-CATEGORY / Platoon snapshot, including the full §13 stat cards and weapon library. I did not audit it line by line, because it is stale *wholesale* by the bible's own admission; every orphan above exists there too, plus the roster (§13) and naming (§14) sections the bible defers to. Treat as regenerate, not edit.

---

## 3. Orphan catalogue — game & catalogue files

### `PraxisBelli.gst` (65 shared rules, 13 category entries, revision 2)

| Area | Finding |
|---|---|
| **Architecture** | 12 of 13 `categoryEntry` items exist to bundle rules onto TYPE/CATEGORY (Armor, Command, Line, Recon, Shock, Support + Infantry, Cavalry, Vehicle, Monster, Aerial, Towable). Under Role/Keyword these become plain keywords/roles with **no `infoLinks`**. Only `Aura` is unrelated. |
| **Characteristic name** | Unit Profile still has **`Wounds`**; docs say **`Toughness`**. [DRIFT] |
| **Die- or scale-dependent (rewrite)** | ~9: `Blast (S)`, `Blast (L)` (scatter dice), `Overcharge` (1d5; docs say Damage-1 hit), `Regeneration` (1d5), `Guided` (still −3 EVA; bible is "flat 3+"), `Shrugs` (d10), `Lance` (+2 AP; bible +1), `Crushing`, `Crushing Impact` (AP3/D2 on a 0–4 scale). |
| **Range-band-dependent** | `Shotgun`, `Meltdown`, `Accurate` (rerolls 1s; bible: ignores range), `Optics` (.gst: no long-range penalty, which is now the *same job as Accurate*; bible: ignore Obscuring evasion bonuses). |
| **Morale-touching** | `Fearless` (still old bundled text incl. "ignores deteriorating morale"), `Entrenched` (rerolls Morale tests instead of granting `Courage`), `Mindless`, `Undaunted`, `Rallying Cry`, `Terrifying`, `Inspiring Leadership`. |
| **Survive unchanged (~30)** | Pistol, Indirect, Smoke, Engulf, Heavy, Turret, three Arcs, Suppressing, Coaxial, Linked-Weapon, Bombardment, Traversing, Indomitable, Ablative Plating, Consumable, Onslaught, Bodyguard, Negates, Impact, Anti-, Transport, Open/Closed-Topped, Sharpshooter, Ravaging, Flying, Soaring Above, etc. |
| **In the game, not in the docs** | `Sharpshooter`, `Resurrect` (docs call it `Divine Favor`), `Ravaging` (mentioned once in prose, not glossary), `Smoke` (as a shared rule). **Bible open-thread #10** already lists ~30 rules that go the *other* direction (docs → .gst). |

### `Imperial Regiments.cat` (11 units, 20 weapon profiles, rev 1)

- **It's the placeholder roster**: old names, old d10 stat lines, **no Massed Ranks**, no Mustelidae vehicles, no Dragoon/Sapper/Hunter.
- Off-scale after conversion: AFV **Armor 7**, Tank Destroyer **Armor 8**, Storm Squad and Scout **Evasion 7**, Main Cannon **AP5**, Laser Cannon **AP6**.
- Two rule links have stale display names (`Leadership Aura`, `Trailor` → resolve to `Inspiring Leadership`, `Trailer`); IDs are fine, so nothing is broken, just cosmetic.
- **Effectively 100% stale. Nothing worth preserving except the force-entry scaffolding.**

### `Imperial Saints.cat` (8 unit profiles, 32 weapon profiles, 48 non-zero costs, rev 5)

- The **most built-out** file (95 KB), and by design the most valuable: it holds real NewRecruit *machinery* (61 selection entries, 18 groups, 68 modifiers, 50 constraints, 35 entry links) implementing squad/special-weapon/sergeant decrement structures.
- **The structure is reusable; the numbers are not.** Off-scale: Prophesier MBT & Pilgrim APC **Armor 12**, Ascendant Warsuits **Armor 7**, Fanatical Sisters **Eva 7**, Battle Cannon **AP5**, Prosecution Cannon **AP7**, Heavy Fusion Blaster **AP8**, infantry Fusion Blaster **AP8**. Every cost is a d10 output. Several unit entries have **no cost on the parent** (costs live on children).
- `Martyrs, All` rule text ("falls below half its starting total wounds") is fine, but its priced multiplier and morale-reroll interplay with the redesign need a look.
- **Effectively: keep the skeleton, re-stat every leaf.**

### `Wrathbound Oathbreakers.cat` (1 unit, rev 1)

- One unit (Berserker Legionaries: Spd7 / Met5 / **Eva3** / **Arm6** / W2), **no cost**.
- **Two rules that disagree with the docs:** `Wrathbound` here = "rerolls failed **damage** rolls in melee" only (docs: melee damage **and** morale rerolls); and **`Tithe of Skulls`** (ignore suppression on Morale tests, forced charge, grants `Extra Hits 8+` after a kill) — **appears nowhere in any document.** The `.cat` is ahead of the docs here, consistent with the bible's "NewRecruit is default source of truth outside design sessions" rule; but that rule says this is a conflict to *surface*, so: surfacing it. `Extra Hits 8+` is also unreachable on d6.
- Eva3 on infantry breaks the Infantry=5 template.

### `Imperial Oathkeepers.cat`

Empty stub. Nothing to orphan. The full Oathkeeper roster (13 named units/vehicles) lives only in prose.

### Tooling (`points.py`, `build_cat.py`, `factions/imperial_regiments.json`)

- `points.py`: `p_hit` = `(11 − evasion)/10` clamped 0.1–0.9, `p_damage` cascade at 10, `EVASION_CAP = 9`, all calibration constants — **the probability core is 2 functions and 1–2 tables**; the rest (trait tiers, size factor, transport, reference roster) is die-independent and reusable. So it's a **rewrite of a core, not of a program.**
- `build_cat.py` and the JSON schema are **not d10-dependent**, but the JSON *content* is the 11-unit old roster. Per your standing decision you hand-build `.cat` entries, so these are reference/staging tools; low priority.

### Housekeeping on the game side

- `gameSystemRevision` in `Imperial Regiments.cat`, `Imperial Saints.cat`, `Imperial Oathkeepers.cat` = 1; the `.gst` is at revision 2 (`Wrathbound` at 2). Probably harmless, but worth knowing given the revision-bump workflow.

---

## 4. Effort estimate (rough; relative, not calendar)

Size dominated by **decisions**, not typing. "S" = a sitting, "M" = a few, "L" = a project.

| Piece | Verdict | Size | What dominates cost |
|---|---|---|---|
| Bible §0–§6, glossary | Edit in place | **M** | Deciding B1/B3/B5/B9/B10 answers; then notation sweeps |
| Bible §7, §8, §10 | **New write** | **M** | Role/Keyword namespace, CORE bonuses (undecided) |
| Bible §11 (points) | **New write** | **L** | Recomputing tables *and* calibrating to 100 pts at 80/20 |
| `faction-identity.md` | Overhaul in place | **L** (wide, shallow) | Vehicle/roster prose needs a notation + terminology sweep (~90 lines touch TYPE/CATEGORY or AP/Armor/Evasion numerics); ~10 real conceptual rewrites (A7, A9, B3–B5, C3, D1) |
| `points.py` | Rewrite the core, keep the shell | **S–M** | Deciding the probability model; code is small |
| `PraxisBelli.gst` | Overhaul, **keep IDs** (the `.cat`s link by ID) | **M** | ~25 rules rewritten; ~30 unchanged; categories stripped of links |
| `Imperial Regiments.cat` | **Rebuild** | **L** | Whole roster (11 old placeholders → roughly 20 named units + vehicles) by hand |
| `Imperial Saints.cat` | **Re-stat the skeleton** | **M–L** | 8 units × loadouts of leaf values |
| `Wrathbound .cat` | Rebuild | **S** | 1 unit; needs the `Tithe of Skulls` decision first |
| `Oathkeepers .cat` | Build new | **L** | 13 units/vehicles, all prose today |
| `reference.html` | **Regenerate** | **M** | Only after the bible stabilises |

---

## 5. Decisions that gate the work (in order)

> **Update, same day:** items 1–7 below and both small confirmations were answered in conversation. The answers, plus the follow-up questions they raised, are recorded in the bible's **"Resolved 2026-09-28"** block under the Decision Queue. The range-band items (B10, B11) were applied to `design-bible.md` and the Oathkeeper Scattergun line in `faction-identity.md`. The list is kept below as the original question record.
>
> **Update, Round 2 (same day):** follow-up questions from Round 1 were answered and recorded in the bible's **"Round 2"** sub-block. Net effect on this audit: B13 (`Extra Hits (X)`/`Critical (X)` thresholds) is resolved for `Extra Hits` (flat, natural-6-only — no more `X`) but still open for `Critical (X)`. C5's faction-signature-trait scope question is narrowed: `Tithe of Skulls` drops its suppression-immunity clause specifically because `Fearless` already covers it faction-wide — a real example of the "rare, expensive, faction-signature" principle being applied rather than just stated. A2 (objective claim/contest) is resolved: non-INFANTRY units may now claim, but only by spending their Combat action, so §9.1 needs a rewrite, not a deletion. `ProjectSummary.md` (item G) was rewritten. The 1000-point anchor throughout §0/§8/§11 (D4, E2) is now explicitly unsettled rather than merely stale — don't assume 1000 when eventually rebuilding §11.

Answering these unblocks nearly everything mechanical.

1. **Role vs Keyword namespace.** Are Role names (LINE, ARMOR, RECON…) also Keywords? (Gates A3, A4, A5 and every `Anti-Line/Armor/…` and `Guided`/`Indirect` sentence.)
2. **Where do objective claim/contest rules live** once TYPE grants nothing? (A2. It's the game's main combined-arms lever.)
3. **Evasion keyed on what?** And does the Rifle Squad anchor sit at Eva5 (template) or Eva6 (current)? Is Light Chassis exempt from "Light Vehicle 3–4"? (B1–B4.)
4. **AP scale final?** If 0–4, do AT weapons re-scale or lean on `Anti-*` and Damage instead? (B9.)
5. **`Accurate`, range bands, `Shotgun`/`Meltdown`** — one pass to make the +1/+0/−1 language consistent. (B10, B11.)
6. **CORE bonus per Role** (queue item 3, undecided).
7. **Mettle range for d6** and what happens to redundant `Courage`/`Fearless`/auto-pass stacking on Met 6–7 units. (B16.)

Plus two small confirmations: **Iron Horizon** (dead name?) and the Wrathbound `.cat`'s **`Tithe of Skulls`** (keep, and document?).

---

## 6. Suggested sequence

1. Decide §5 items 1–7 (design conversation, no file edits).
2. Bible: rewrite §7, §8, §10, §11; edit §0–§6 and glossary; delete/resolve Open Threads.
3. `points.py` core → recalibrate the 100-pt anchor → freeze numbers.
4. `.gst` sweep (keep IDs).
5. `faction-identity.md` sweep (notation first, then the ~10 conceptual rewrites).
6. Stat lines derived from identity, then `.cat` entries by hand (Saints skeleton first, since it's furthest along).
7. Regenerate `reference.html` last, or retire it and let the bible be the single source (it's the main drift generator).

**Do not** touch `.cat` numbers before step 3 is frozen; that's the one ordering mistake that would cost real rework.
