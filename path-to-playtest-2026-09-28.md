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

3. **Update `points.py` to match §11.** Right now the bible is ahead of the code — `BASE_MODEL`, `BASE_WEAPON`, the sqrt-dampened Evasion/Armor/Mettle tables, the corrected overkill cap, and the dropped AP-volume-premium term all need to land in the actual calculator before anyone can price a real unit by hand against it.
4. **Classify the weapon traits and named abilities that the *first playtest faction* actually uses**, not the whole glossary. Only a first-pass example set exists for each tier system (Step 3 and Step 5 of §11) — `Blast`, `Engulf`, `Indirect`, `Barrage`, `Crushing`, `Shotgun`, `Meltdown`, `Lance`, `Impact (X)`, `Consumable (X)`, `Shrug (X)`, `Undaunted (X)`, `Combat Medic`, `Picket`, `Negates`, `Bodyguard` and the rest are all still unclassified. Scope this to whichever faction gets picked in Phase 3 — classifying the other ~20 traits nobody's using yet is Outstanding Work, not a blocker.
5. **Pick a placeholder standard-game point total.** 1000 vs. 2000 vs. 3000 is still open — for a first playtest, pick a working number for that specific game rather than waiting on the permanent answer. Nothing about the formula depends on this being final.

### Phase 3 — Get one faction fully re-priced and playable

**Recommend Imperial Saints.** It's furthest along in shape and identity — vehicles, warsuits, and four of its infantry units already had a full package/identity pass before the v0.5 redesign started, and its own roadmap note already said "leadership is next, then Saints is ready for playtesting." Re-doing that identity work from scratch on a less-finished faction would cost more than re-pricing Saints against the new mechanics.

**The fastest real game is a mirror match** — Saints vs. Saints needs only *one* faction fully done, not two, and still exercises every core mechanic (dice, morale, Damage Track, Platoons/CORE, Transports, objectives).

6. Re-audit every Saints unit's **Role** against what it's actually expected to do on the battlefield (per the Round 1 instruction — this was flagged project-wide, never done unit-by-unit).
7. Assign **Keywords** per unit (Infantry/Vehicle/Monster as appropriate, plus any faction-specific ones already named — `Caster`, etc.).
8. Re-derive each unit's stat line against the **Evasion archetype template** (§3) and the now-locked Armor/Wounds/Speed/Mettle factor tables — confirming which of Saints' existing "shape, not numbers" stat lines still make sense once Evasion is templated rather than freely tuned (Saints' own Armor/Evasion pairing was flagged as one of the units affected by this back in the faction-identity sweep).
9. **Price every unit and weapon** against the finalized §11 formula (once Phases 2–4's classification work covers what Saints actually needs) and write the real numbers into `Imperial Saints.cat`.

### Phase 4 — Play it

Saints vs. Saints, the one mission from Phase 1, the placeholder point total from Phase 2. Whatever breaks, breaks *after* a real game, with real data — not before one.

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
