# Praxis Belli

A combined-arms tabletop miniatures wargame — d10 roll-over engine, alternating activation, Platoon-based list building. Built to run parallel to grimdark-adjacent settings (own arcanepunk fiction, deliberately 40k-shaped silhouettes) without requiring anyone to own a specific manufacturer's models: the **proxy contract** is a binding design rule that an existing collection should always be playable as-is, and a new collector should never be steered toward one company.

This repo holds both the **NewRecruit / BattleScribe data** for building army lists and the **design toolchain** that prices and generates it: the game system definition, faction catalogues, the points formula as executable code, a generator that turns a faction spec into a priced `.cat`, and the working rules/lore reference.

## Status

**Pre-alpha, actively changing.** Stat lines, weapon profiles, and points values in these files should be treated as scratch — they get rewritten often as the underlying rules evolve. Nothing here is balanced or final. If you're picking this up cold, check the most recent commit dates before trusting a specific number.

## What's in this repo

| File | Contents |
|---|---|
| `PraxisBelli.gst` | The game system: CATEGORY and TYPE keywords, stat block templates (Unit Profile, Weapon Profile), and every shared rule (Anti-[Keyword], Suppressing, Transport, Entrenched, etc.) |
| `Imperial Regiments.cat` | The most developed faction — massed conscript infantry backed by flexible armor. Full roster: Command, Line, Recon, Shock, Support, and Armor units. |
| `Imperial Saints.cat` | Stub. Faction shared rule only (`Blessed by Devotion`); no units yet. |
| `Imperial Oathkeepers.cat` | Stub. Catalogue shell only; no content yet. |
| `design-bible.md` | The full ruleset and its rationale — every mechanic, why it's shaped that way, and what's still open. |
| `reference.html` | The same content as `design-bible.md`, laid out as a single-page reference. Also published as a Claude Artifact; keep both in sync when either changes. |
| `faction-identity.md` | Faction and setting design — the Sworn Empire cosmology, per-faction mechanical identity, naming conventions, roadmap. |
| `points.py` | The points formula as runnable code. `python points.py` costs a built-in reference roster; import `cost_unit`/`weapon_cost`/`model_cost` to price anything else. |
| `build_cat.py` | Reads a faction JSON (see `factions/`), prices every unit via `points.py`, and writes a valid `.cat` straight into this folder. Resolves category/rule/profile IDs by name from `PraxisBelli.gst` at build time and derives entry IDs from the unit name, so rebuilds don't churn the file. |
| `factions/*.json` | Compact faction definitions (shared weapon library + unit list) — edit stats here, never points; points are always regenerated. |

This folder **is** the live data directory NewRecruit reads from — there's no build or deploy step for the `.cat`/`.gst` files themselves. Editing one and reloading NewRecruit is the whole workflow. Regenerating a faction from its JSON is `python build_cat.py factions/<name>.json`.

## The setting, in one paragraph

Magic here is *sworn*, not cast: an oath kept channels power, an oath broken inverts into something worse. The **Sworn Empire** is the oath-network itself, not a state that merely uses it — citizenship is a contract position, and "Chaos" is simply the breaking of the First Binding that holds the plane together. Imperial factions are tiers of binding (Regiments' shallow Levy Oath, the Oathkeepers' unbreakable Deep Oath, and so on); the Oathbreaker Legions are that same Deep Oath inverted. Xenos factions are defined by how they sit *outside* the network entirely.

## Faction naming conventions (Imperial Regiments)

Two deliberately contrasting themes: **vehicles get predator nicknames** (what the factory built), **infantry get martial titles** (what the soldier earned or was assigned).

- Vehicle chassis: Mustelidae (weasel family) — Stoat, Weasel, Mink (light); Marten, Sable, Fisher, Tayra (medium); Wolverine (the one bespoke tank-killer, deliberately not part of the family).
- Infantry: Levy (conscripts — the name is pulled directly from their in-fiction Levy Oath), Fusilier (line), Grenadier (veteran), Vanguard (shock), Ranger (recon), Ballistier (flexible heavy weapons, provisional name), Sapper (combat engineer), Hunter (anti-tank), Dragoon (mechanized — rides any friendly Transport via *Rapid Deployment*, its answer to why Regiments is the combined-arms template faction).

## Working with this repo

- Points values are formula-derived, not hand-tuned. If you're pricing something new, use `points.py` rather than picking a number by feel — and if you change a constant in it, re-check the anchor (a 10-model Rifle Squad with rifles and bayonets should land on 100 points) before trusting anything else it outputs.
- The sibling folder `Praxis Belli` (with a space, if you have it checked out elsewhere) is an **older, superseded game system** — do not merge content from it into this one; the two use different game system IDs.
- `design-bible.md`/`reference.html` and `faction-identity.md` are living documents — update them in the same commit as the mechanic or decision they describe, not after the fact.
