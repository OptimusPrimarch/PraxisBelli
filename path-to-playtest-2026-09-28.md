# Path to Playtest — 2026-09-28

A working checklist, not a design document. Everything here is either "must happen before a first game" or "tracked so it doesn't get lost, but doesn't block one." When in doubt about ordering: **can two people actually sit down and play with this missing? If yes, it's Outstanding Work, not Path to Playtest.**

---

## Path to First Playtest

Four phases, roughly sequential — each one is the shortest route to an actual game, not the most thorough version of the work.

### Phase 1 — Close the two rules gaps that block *any* game ✅ Done (2026-09-28)

Both were Open Threads sitting unaddressed since before the v0.5 redesign even started.

1. ~~Write a minimal Facings/Arcs section.~~ **Done** — §6's new Facing & Arcs subsection. Covers ordinary play, not every corner case.
2. ~~Design one mission.~~ **Done** — "Claim the Ground," §9. One working scenario, not the full planned 5–10.

### Phase 2 — Make the points formula load-bearing, not just correct

The formula (§11) is solid as of the 2026-09-28 rebuild, but nothing has actually been priced with it yet.

3. ~~Update `points.py` to match §11.~~ **Done (2026-09-28)** — full bare-slate rewrite: new `BASE_MODEL`/`BASE_WEAPON`, sqrt-dampened Evasion/Armor/Mettle factors, corrected overkill cap, AP-volume-premium term dropped, CCW flat-0, three-tier trait/ability system, additive `anti_keyword_surcharge()`, seat-based transports, flat (no-discount) unit size scaling. Verified by hand against the Rifle Squad anchor: 79.98 chassis + 20.00 weapons = 99.98 ≈ 100, matching §11 exactly.
4. **Classify the weapon traits and named abilities that the *first playtest faction* actually uses**, not the whole glossary. Only a first-pass example set exists for each tier system (Step 3 and Step 5 of §11) — `Blast`, `Engulf`, `Indirect`, `Barrage`, `Crushing`, `Shotgun`, `Meltdown`, `Lance`, `Impact (X)`, `Consumable (X)`, `Shrug (X)`, `Undaunted (X)`, `Combat Medic`, `Picket`, `Negates`, `Bodyguard` and the rest are all still unclassified. Scope this to whichever faction gets picked in Phase 3 — classifying the other ~20 traits nobody's using yet is Outstanding Work, not a blocker.
5. **Pick a placeholder standard-game point total.** 1000 vs. 2000 vs. 3000 is still open — for a first playtest, pick a working number for that specific game rather than waiting on the permanent answer. Nothing about the formula depends on this being final.

### Phase 3 — Get one faction fully re-priced and playable

**Faction chosen: Imperial Regiments** (2026-09-28 — the user confirmed either Saints or Regiments works for the mirror match; Regiments is the one actually being built). **The fastest real game is a mirror match** — Regiments vs. Regiments needs only *one* faction fully done, not two, and still exercises every core mechanic (dice, morale, Damage Track, Platoons/CORE, Transports, objectives).

**Phase 3a — watered-down slice, done (2026-09-29).** Per the user's own scoping ("just enough to see the system in motion... not the whole faction"): **Rifle Squad, Veteran Squad, Scout Element, Armored Personnel Carrier, Armored Fighting Vehicle** (Fusilier/Grenadier/Ranger/the APC/treated as the MBT). All five re-priced end to end in `factions/imperial_regiments.json` and regenerated into `Imperial Regiments.cat`:
6. ~~Re-audit Role~~ — all five already carried the right Role (design-bible.md §7 literally cites the APC as SUPPORT/Vehicle and the AFV as ARMOR/Vehicle as its own worked examples); no changes needed.
7. ~~Assign Keywords~~ — same result, all five already correct (Infantry ×3, Vehicle ×2).
8. ~~Re-derive stat lines against the Evasion archetype template~~ — done: all three infantry locked to Evasion 5 (Scout Element deliberately uses the "Elite/dedicated dodge specialist" archetype row instead, Evasion 6, not a veterancy tweak); the two vehicles moved to the Light/Heavy Vehicle archetype band (Evasion 5 and 3 respectively) instead of freely-tuned old-data values.
9. ~~Price every unit and weapon~~ — done (Rifle Squad 106, Veteran Squad 125, Scout Element 82, APC 151, AFV 238). Along the way, found and fixed two real bugs blocking this: `build_cat.py` was reading a `toughness` characteristic the `.gst` had already renamed to `Wounds` (crashed on any rebuild), and the faction's old top-level `Massed Ranks` `faction_trait` was auto-applying to every 8+-model unit even though §8's Round 3 decision already moved it to a Platoon-CORE bonus — both fixed, not just worked around.

**Phase 3b — the rest of the faction, not started.** Regimental Officer, Conscript Mob, Storm Squad, Heavy Weapons Team, Field Gun Battery, Tank Destroyer, plus Sapper/Hunter/Dragoon (no stat lines yet at all). Needed before a *full* Regiments list is legal, not needed for the mirror-match slice above.

### Phase 4 — Play it

Regiments vs. Regiments, the one mission from Phase 1, the placeholder point total from Phase 2 (item 5 — still not picked). The watered-down Phase 3a slice is playable as a small mirror match right now; a full-list game still needs Phase 3b.

---

## Outstanding Work

Not blocking. Tracked so it doesn't get lost once Phase 4 happens and momentum shifts to "what's next."

**Formula refinement**
- The range multiplier (`0.6 + Range/30`) has never been re-derived — it doesn't connect to the Close/Effective/Long bands at all, just carried forward as a placeholder.
- Exhaustive trait/ability classification beyond whatever Phase 2 needed for Saints specifically.
- The four faction signature-trait multipliers (`Oathbound`, `Bound Spirit`, `Martyrs, all`, `Wrathbound`) still need real numbers against the new formula, not d10-era guesses.
- `Regiments needs a new faction signature trait` — `Massed Ranks` moved to being a Platoon CORE bonus, vacating that slot. Deliberately deferred multiple times now; still open.
- §4's own `Fists`→`CCW` section still says "Fists" in its prose — the decision (0 points, fixed) is made, the text isn't updated.

**Roster completion (after Saints is playable)**
- **Imperial Regiments**: still the placeholder 11-unit roster in `.cat`/JSON — the Levy/Fusilier/Grenadier naming pass was decided but never applied to the actual data; the full Mustelidae vehicle family (Marten/Sable/Fisher/Tayra/Stoat/Weasel/Mink/Wolverine/Badger) exists only as prose; Sapper/Hunter/Dragoon have locked identities and no stat lines.
- **Wrathful Oathbreakers**: one unit (`Berserker Legionaries`) — needs a real roster (at minimum a troop and a heavy/elite choice) before it can field a full list, not just re-pricing.
- **Imperial Oathkeepers**: `.cat` is an empty stub. Full roster (13 named units/vehicles) exists only in `faction-identity.md` prose.
- **Imperial Forgesworn**: named and hooked, nothing built.
- **Xenos factions** (Unspoken, Interred, Thornbound, Scrapjaw Hordes): stubs only, explicitly "later" work per the existing roadmap.

**Documentation sync**
- `PraxisBelli.gst` is still missing ~30 rules that already exist in the design-bible glossary and faction-identity.md (Open Thread #10's list) — matters once NewRecruit needs to be the thing players read rules off of at the table, not blocking if `design-bible.md` itself serves as the rulebook for the first game.
- `reference.html` is still a complete stale snapshot — regenerate once the bible stabilizes further, not before.
