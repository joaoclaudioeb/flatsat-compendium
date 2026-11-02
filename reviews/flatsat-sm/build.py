"""Generate README.md from data/flatsat_platforms.csv and data/references.bib.

Usage: python build.py   (standard library only)
Edit the CSV/.bib, never the README: it is overwritten.
"""
import csv
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
CSV = HERE / "data" / "flatsat_platforms.csv"
BIB = HERE / "data" / "references.bib"

HEADER = """# FlatSat platforms: systematic mapping (2023)

Platforms and works analyzed in the systematic mapping of FlatSat platforms for small satellites.

Publication: J. C. E. Barcellos *et al.*, "FlatSat Platforms for Small Satellites: A Systematic Mapping and Classification," *IEEE J-MASS*, vol. 4, no. 2, pp. 186–198, 2023, doi: [10.1109/JMASS.2023.3249044](https://doi.org/10.1109/JMASS.2023.3249044).

## Files

- `data/flatsat_platforms.csv` — one row per analyzed work (columns below)
- `data/references.bib` — BibTeX entries of the analyzed works (key = `bibkey`)
- `build.py` — regenerates this README (do not edit it by hand)

## Columns

| Column | Meaning |
|---|---|
| `id` | Work number in the original screening |
| `bibkey`, `title`, `year`, `venue`, `link` | Bibliographic data |
| `mission`, `project` | Mission or project the platform was built for |
| `type` | `raw`, `bridge`, `dock`, or `modular` (`;` if more than one) |
| `assembly` | `wire_harness` and/or `backplane` |
| `support_structure` | Another structure (metallic or not) supports the platform |
| `backplane` | `passive` or `active` (backplane-based platforms only) |
| `sensors` … `cpld` | Backplane features (backplane-based platforms only) |
| `test_*` | Tests conducted with the platform |
"""


def first_author(bib, key):
    m = re.search(r"@\w+\s*\{\s*" + re.escape(key) + r"\s*,(.*?)\n\}", bib, re.S)
    if not m:
        return key
    a = re.search(r"author\s*=\s*\{(.*?)\}\s*,?\s*(?:\n|$)", m.group(1), re.S)
    if not a:
        return key
    names = a.group(1).split(" and ")
    last = names[0].split(",")[0].replace("{", "").replace("}", "").strip()
    return last + (" et al." if len(names) > 1 else "")


def main():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    bib = BIB.read_text(encoding="utf-8")
    n = len(rows)
    types = Counter(t for r in rows for t in r["type"].split(";"))
    tests = {c[5:]: sum(r[c] == "yes" for r in rows) for c in rows[0] if c.startswith("test_")}

    out = [HEADER, "## Summary\n", f"{n} works analyzed.\n"]
    out.append("| Type | Works |\n|---|---|")
    out += [f"| {t.capitalize()} | {types[t]} |" for t in ("raw", "bridge", "dock", "modular")]
    out.append("\n| Test | Works |\n|---|---|")
    out += [f"| {t.upper() if t == 'emc' else t.capitalize()} | {v} |" for t, v in tests.items()]
    out.append("\nWorks with more than one type are counted in each.\n")

    bp = [r for r in rows if "backplane" in r["assembly"].split(";")]
    labels = {"support_structure": "Supporting structure (all works)",
              "passive": "Passive backplane", "active": "Active backplane",
              "sensors": "Sensors (e.g., power consumption, temperature)",
              "switches_jumpers": "Switches and/or jumpers",
              "ext_power_connectors": "Connectors for external power supplies",
              "monitoring_points": "Connectors, LEDs, and/or test points for monitoring",
              "std_connectors": "Other standardized connectors (e.g., USB, antenna)",
              "cpld": "CPLD"}
    out.append(f"| Platform characteristic | Works |\n|---|---|")
    out.append(f"| {labels['support_structure']} | {sum(r['support_structure'] == 'yes' for r in rows)} |")
    out.append(f"| Backplane-based platforms | {len(bp)} |")
    for k in ("passive", "active"):
        out.append(f"| &nbsp;&nbsp;{labels[k]} | {sum(r['backplane'] == k for r in bp)} |")
    for k in ("sensors", "switches_jumpers", "ext_power_connectors", "monitoring_points", "std_connectors", "cpld"):
        out.append(f"| &nbsp;&nbsp;{labels[k]} | {sum(r[k] == 'yes' for r in bp)} |")
    out.append("")

    out.append("## Works\n")
    out.append("| # | Work | Mission / project | Type | Backplane features | Tests |\n|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: (r["year"], r["bibkey"])):
        name = f"{first_author(bib, r['bibkey'])} ({r['year']})"
        work = f"[{name}]({r['link']})" if r["link"] else name
        mp = r["mission"] or r["project"] or "—"
        ty = ", ".join(t.capitalize() for t in r["type"].split(";"))
        te = ", ".join(c[5:].upper() if c == "test_emc" else c[5:].capitalize()
                       for c in r if c.startswith("test_") and r[c] == "yes") or "—"
        feats = [r["backplane"].capitalize()] if r["backplane"] else []
        feats += [n for c, n in (("sensors", "sensors"), ("switches_jumpers", "switches"),
                                 ("ext_power_connectors", "power conn."), ("monitoring_points", "monitoring"),
                                 ("std_connectors", "std. conn."), ("cpld", "CPLD")) if r[c] == "yes"]
        out.append(f"| {r['id']} | {work} | {mp} | {ty} | {', '.join(feats) or '—'} | {te} |")

    (HERE / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"README.md written ({n} works)")


if __name__ == "__main__":
    main()
