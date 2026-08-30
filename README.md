# Praxis Belli

A combined-arms tabletop miniatures wargame — d10 roll-over engine, alternating activation, Platoon-based list building. Built to run parallel to grimdark-adjacent settings (own arcanepunk fiction, deliberately 40k-shaped silhouettes) without requiring anyone to own a specific manufacturer's models: the **proxy contract** is a binding design rule that an existing collection should always be playable as-is, and a new collector should never be steered toward one company.

This repo is the **NewRecruit / BattleScribe data** for building army lists — the game system definition and faction catalogues. It is not the rulebook. The full ruleset, points formula, and design rationale live in a separate working reference; this repo is specifically the machine-readable roster data that reference gets transcribed into.

## Status

**Pre-alpha, actively changing.** Stat lines, weapon profiles, and points values in these files should be treated as scratch — they get rewritten often as the underlying rules evolve. Nothing here is balanced or final. If you're picking this up cold, check the most recent commit dates before trusting a specific number.

## What's in this repo

| File | Contents |
|---|---|
| `PraxisBelli.gst` | The game system: CATEGORY and TYPE keywords, stat block templates (Unit Profile, Weapon Profile), and every shared rule (Anti-[Keyword], Suppressing, Transport, Entrenched, etc.) |
| `Imperial Regiments.cat` | The most developed faction — massed conscript infantry backed by flexible armor. Full roster: Command, Line, Recon, Shock, Support, and Armor units. |
| `Imperial Saints.cat` | Stub. Faction shared rule only (`Blessed by Devotion`); no units yet. |
| `Imperial Oathkeepers.cat` | Stub. Catalogue shell only; no content yet. |

This folder **is** the live data directory NewRecruit reads from — there's no build or deploy step. Editing a file here and reloading NewRecruit is the whole workflow.

## The setting, in one paragraph

Magic here is *sworn*, not cast: an oath kept channels power, an oath broken inverts into something worse. The **Sworn Empire** is the oath-network itself, not a state that merely uses it — citizenship is a contract position, and "Chaos" is simply the breaking of the First Binding that holds the plane together. Imperial factions are tiers of binding (Regiments' shallow Levy Oath, the Oathkeepers' unbreakable Deep Oath, and so on); the Oathbreaker Legions are that same Deep Oath inverted. Xenos factions are defined by how they sit *outside* the network entirely.

## Faction naming conventions (Imperial Regiments)

Two deliberately contrasting themes: **vehicles get predator nicknames** (what the factory built), **infantry get martial titles** (what the soldier earned or was assigned).

- Vehicle chassis: Mustelidae (weasel family) — Stoat, Weasel, Mink (light); Marten, Sable, Fisher, Tayra (medium); Wolverine (the one bespoke tank-killer, deliberately not part of the family).
- Infantry: Levy (conscripts — the name is pulled directly from their in-fiction Levy Oath), Fusilier (line), Grenadier (veteran), Vanguard (shock), Ranger (recon), Ballistier (flexible heavy weapons, provisional name), Sapper (combat engineer), Hunter (anti-tank), Dragoon (mechanized — rides any friendly Transport via *Rapid Deployment*, its answer to why Regiments is the combined-arms template faction).

## Working with this repo

- Points values are formula-derived, not hand-tuned — see the companion design reference for the actual formula (`points.py` in the main project workspace) if you're pricing something new by hand in the meantime.
- The sibling folder `Praxis Belli` (with a space, if you have it checked out elsewhere) is an **older, superseded game system** — do not merge content from it into this one; the two use different game system IDs.
