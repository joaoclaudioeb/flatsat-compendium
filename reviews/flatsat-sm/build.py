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

    out.append("## Works\n")
    out.append("| # | Work | Mission / project | Type | Tests |\n|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: (r["year"], r["bibkey"])):
        name = f"{first_author(bib, r['bibkey'])} ({r['year']})"
        work = f"[{name}]({r['link']})" if r["link"] else name
        mp = r["mission"] or r["project"] or "—"
        ty = ", ".join(t.capitalize() for t in r["type"].split(";"))
        te = ", ".join(c[5:].upper() if c == "test_emc" else c[5:].capitalize()
                       for c in r if c.startswith("test_") and r[c] == "yes") or "—"
        out.append(f"| {r['id']} | {work} | {mp} | {ty} | {te} |")

    (HERE / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"README.md written ({n} works)")


if __name__ == "__main__":
    main()
