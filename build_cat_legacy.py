"""
Build a NewRecruit / BattleScribe .cat catalogue from a compact faction JSON,
pricing every unit with the formula in points.py.

    python build_cat.py factions/imperial_regiments.json

IDs are derived deterministically from names, so rebuilding a faction keeps the
same IDs and does not churn the file. Reads the .gst at build time to resolve
category / profile-type / rule IDs by name, so it self-corrects if those move.
"""

import hashlib
import html
import json
import os
import sys
import xml.etree.ElementTree as ET

from points import cost_unit, model_cost, weapon_cost, transport_cost

BS_NS = "http://www.battlescribe.net/schema/catalogueSchema"
GST_PATH = os.path.expanduser(
    r"~\Documents\NewRecruit\data\PraxisBelli\PraxisBelli.gst"
)
OUT_DIR = os.path.expanduser(r"~\Documents\NewRecruit\data\PraxisBelli")


# ------------------------------------------------------------------ ids

def mkid(*parts):
    """Deterministic BattleScribe-style id from a seed string."""
    h = hashlib.md5("|".join(parts).encode()).hexdigest()
    return f"{h[0:4]}-{h[4:8]}-{h[8:12]}-{h[12:16]}"


# ------------------------------------------------------- game system probe

def load_gst(path):
    """Pull the ids we need out of the game system, keyed by name."""
    tree = ET.parse(path)
    root = tree.getroot()
    ns = {"b": root.tag.split("}")[0].strip("{")}

    gs = {
        "id": root.get("id"),
        "revision": root.get("revision", "1"),
        "categories": {},
        "rules": {},
        "profileTypes": {},
        "costType": None,
    }

    for c in root.findall(".//b:categoryEntry", ns):
        gs["categories"][c.get("name").lower()] = c.get("id")

    for r in root.findall(".//b:rule", ns):
        gs["rules"][r.get("name").lower()] = r.get("id")

    for pt in root.findall(".//b:profileType", ns):
        chars = {
            ct.get("name").lower(): ct.get("id")
            for ct in pt.findall("b:characteristicTypes/b:characteristicType", ns)
        }
        gs["profileTypes"][pt.get("name").lower()] = {
            "id": pt.get("id"), "chars": chars,
        }

    ct = root.find(".//b:costType", ns)
    if ct is not None:
        gs["costType"] = {"id": ct.get("id"), "name": ct.get("name")}

    return gs


# ------------------------------------------------------------ xml helpers

def esc(v):
    return html.escape(str(v), quote=True)


def characteristic(name, type_id, value):
    return (f'<characteristic name="{esc(name)}" typeId="{type_id}">'
            f'{esc(value)}</characteristic>')


def unit_profile(gs, unit):
    pt = gs["profileTypes"]["unit profile"]
    c = pt["chars"]
    p = unit["profile"]
    pid = mkid(unit["name"], "unitprofile")
    rows = "".join([
        characteristic("Speed", c["speed"], f'{p["speed"]}"'),
        characteristic("Mettle", c["mettle"], p["mettle"]),
        characteristic("Evasion", c["evasion"], p["evasion"]),
        characteristic("Armor", c["armor"], p["armor"]),
        characteristic("Toughness", c["toughness"], p["toughness"]),
    ])
    return (f'<profile name="{esc(unit["name"])}" typeId="{pt["id"]}" '
            f'typeName="Unit Profile" hidden="false" id="{pid}">'
            f"<characteristics>{rows}</characteristics></profile>")


def weapon_profile(gs, unit_name, wname, w):
    pt = gs["profileTypes"]["weapon profile"]
    c = pt["chars"]
    pid = mkid(unit_name, "weapon", wname)
    rng = w["range"]
    rng = "M" if str(rng).lower() in ("m", "melee") else f'{rng}"'
    rows = "".join([
        characteristic("Range", c["range"], rng),
        characteristic("Attacks", c["attacks"], w["attacks"]),
        characteristic("Armor Piercing", c["armor piercing"], w["ap"]),
        characteristic("Damage", c["damage"], w["damage"]),
        characteristic("Weapon Traits", c["weapon traits"],
                       ", ".join(w.get("traits", []))),
    ])
    return (f'<profile name="{esc(wname)}" typeId="{pt["id"]}" '
            f'typeName="Weapon Profile" hidden="false" id="{pid}">'
            f"<characteristics>{rows}</characteristics></profile>")


def category_links(gs, unit):
    out = []
    for role, primary in ((unit["category"], "true"), (unit["type"], "false")):
        cid = gs["categories"].get(role.lower())
        if not cid:
            raise KeyError(f"category {role!r} not in game system")
        out.append(
            f'<categoryLink name="{esc(role)}" hidden="false" '
            f'id="{mkid(unit["name"], "cat", role)}" targetId="{cid}" '
            f'primary="{primary}"/>'
        )
    return "".join(out)


def rule_links(gs, unit):
    out = []
    for rname in unit.get("rules", []):
        rid = gs["rules"].get(rname.lower())
        if not rid:
            print(f"  ! warning: rule {rname!r} not in game system, skipped")
            continue
        out.append(
            f'<infoLink name="{esc(rname)}" id="{mkid(unit["name"], "rule", rname)}" '
            f'hidden="false" type="rule" targetId="{rid}"/>'
        )
    return "".join(out)


# ------------------------------------------------------------------ build

def build(faction_path):
    with open(faction_path, encoding="utf-8") as f:
        fac = json.load(f)

    gs = load_gst(GST_PATH)
    lib = fac.get("weapons", {})
    entries = []
    report = []

    for unit in fac["units"]:
        # Resolve weapon references against the faction's shared library.
        resolved = []
        for ref in unit.get("weapons", []):
            wname = ref["name"]
            if wname not in lib:
                raise KeyError(f"weapon {wname!r} not in faction weapon library")
            w = dict(lib[wname])
            w["name"] = wname
            w["count"] = ref.get("count", unit.get("size", 1))
            resolved.append(w)

        priced = dict(unit)
        priced["weapons"] = resolved
        # A faction-wide signature trait applies to every unit unless the unit
        # opts out with "faction_trait": null.
        if "faction_trait" not in priced and fac.get("faction_trait"):
            priced["faction_trait"] = fac["faction_trait"]
        total, lines = cost_unit(priced)
        total = round(total)
        report.append((unit["name"], unit["category"], unit["type"], total, lines))

        profiles = [unit_profile(gs, unit)]
        for w in resolved:
            profiles.append(weapon_profile(gs, unit["name"], w["name"], lib[w["name"]]))

        rules_xml = rule_links(gs, unit)
        infolinks = f"<infoLinks>{rules_xml}</infoLinks>" if rules_xml else ""

        entries.append(
            f'<selectionEntry type="unit" import="true" '
            f'name="{esc(unit["name"])}" hidden="false" '
            f'id="{mkid(unit["name"], "unit")}">'
            f"<categoryLinks>{category_links(gs, unit)}</categoryLinks>"
            f"<profiles>{''.join(profiles)}</profiles>"
            f"{infolinks}"
            f"<costs><cost name=\"{gs['costType']['name']}\" "
            f"typeId=\"{gs['costType']['id']}\" value=\"{total}\"/></costs>"
            f"</selectionEntry>"
        )

    # One permissive force entry accepting every category.
    cat_links = "".join(
        f'<categoryLink name="{n.title()}" hidden="false" '
        f'id="{mkid(fac["faction"], "force", n)}" targetId="{cid}"/>'
        for n, cid in sorted(gs["categories"].items())
    )
    force = (
        f'<forceEntries><forceEntry name="Vanguard Formation" '
        f'id="{mkid(fac["faction"], "forceentry")}" hidden="false">'
        f"<categoryLinks>{cat_links}</categoryLinks></forceEntry></forceEntries>"
    )

    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<catalogue library="false" id="{mkid(fac["faction"], "catalogue")}" '
        f'name="{esc(fac["faction"])}" gameSystemId="{gs["id"]}" '
        f'gameSystemRevision="{gs["revision"]}" revision="1" '
        f'battleScribeVersion="2.03" type="catalogue" xmlns="{BS_NS}">'
        f"<selectionEntries>{''.join(entries)}</selectionEntries>"
        f"{force}"
        "</catalogue>"
    )

    # Pretty-print so the file stays diffable.
    parsed = ET.fromstring(xml)
    ET.indent(parsed, space="  ")
    ET.register_namespace("", BS_NS)
    body = ET.tostring(parsed, encoding="unicode")
    out_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' + body

    out_path = os.path.join(OUT_DIR, fac["faction"] + ".cat")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_xml)

    # Console report.
    print(f"=== {fac['faction']} ===\n")
    grand = 0
    for name, cat, typ, total, lines in report:
        grand += total
        print(f"{name}  [{cat}/{typ}]  -> {total} pts")
        for ln in lines:
            print(ln)
        print()
    print(f"{len(report)} units, {grand} pts of options")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python build_cat.py <faction.json>")
    build(sys.argv[1])
