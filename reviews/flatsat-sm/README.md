# FlatSat platforms: systematic mapping (2023)

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

## Summary

65 works analyzed.

| Type | Works |
|---|---|
| Raw | 41 |
| Bridge | 6 |
| Dock | 18 |
| Modular | 3 |

| Test | Works |
|---|---|
| Functional | 61 |
| Mission | 14 |
| Thermal | 2 |
| EMC | 1 |

Works with more than one type are counted in each.

| Platform characteristic | Works |
|---|---|
| Supporting structure (all works) | 34 |
| Backplane-based platforms | 27 |
| &nbsp;&nbsp;Passive backplane | 22 |
| &nbsp;&nbsp;Active backplane | 5 |
| &nbsp;&nbsp;Sensors (e.g., power consumption, temperature) | 1 |
| &nbsp;&nbsp;Switches and/or jumpers | 10 |
| &nbsp;&nbsp;Connectors for external power supplies | 12 |
| &nbsp;&nbsp;Connectors, LEDs, and/or test points for monitoring | 27 |
| &nbsp;&nbsp;Other standardized connectors (e.g., USB, antenna) | 6 |
| &nbsp;&nbsp;CPLD | 1 |

## Works

| # | Work | Mission / project | Type | Backplane features | Tests |
|---|---|---|---|---|---|
| 56 | Cain et al. (2008) | NTS CubeSat | Raw | — | Functional |
| 23 | [Smith et al. (2008)](https://digitalcommons.usu.edu/smallsat/2008/all2008/81/) | FASTRAC | Raw | — | Functional |
| 83 | [Jackson (2009)](https://doi.org/10.1109/AERO.2009.4839557) | SpaceDev | Raw | — | Functional, Mission |
| 16 | [Pranajaya et al. (2009)](https://digitalcommons.usu.edu/smallsat/2009/all2009/28/) | NTS CubeSat | Raw | — | Mission |
| 59 | Shah (2009) | CanX-2 | Raw | — | Functional, Mission |
| 76 | Lisa A. Baghal (2010) | TacSat-2 | Raw | — | Functional |
| 18 | [Mu\~noz et al. (2010)](https://digitalcommons.usu.edu/smallsat/2010/all2010/76/) | FASTRAC | Raw | — | Functional |
| 15 | Pranajaya et al. (2010) | NTS CubeSat | Raw | — | Mission |
| 33 | Bradbury (2011) | CanX-4 and CanX-5 | Raw | — | Functional |
| 48 | [Mu\~noz et al. (2011)](https://digitalcommons.usu.edu/smallsat/2011/all2011/24/) | FASTRAC | Raw | — | Functional |
| 50 | Urbanek (2011) | CanX-4 and CanX-5 | Raw | — | Functional, Mission |
| 2 | [Samson (2012)](https://doi.org/10.1109/AERO.2012.6187238) | SMDC TechSat | Raw | — | Functional |
| 82 | Johl (2013) | RACE, Bevo-2, and ARMADILLO | Raw | — | Functional, Mission |
| 24 | [Chartres et al. (2014)](https://digitalcommons.usu.edu/smallsat/2014/NextPad/7/) | EDSN | Raw, Bridge | Passive, switches, monitoring | Functional |
| 35 | Cotten (2014) | CanX-7 | Raw | — | Functional |
| 17 | [Johl et al. (2014)](https://doi.org/10.1109/AERO.2014.6836368) | RACE, Bevo-2, and ARMADILLO | Raw | — | Functional, Mission |
| 52 | [\'Oscar R. Polo et al. (2014)](https://doi.org/10.1016/j.actaastro.2013.07.001) | INTA-NanoSat-1B | Raw | — | Functional, Mission |
| 9 | [Samson (2014)](https://doi.org/10.1109/AERO.2014.6836523) | SMDC TechSat | Raw | — | Functional |
| 27 | [S. Busch et al. (2015)](https://doi.org/10.1016/j.actaastro.2015.08.002) | UWE-3 | Dock | Passive, monitoring | Functional |
| 61 | [Stone et al. (2015)](https://doi.org/10.1109/AERO.2015.7119198) | SOAREX-8 | Raw | — | Functional, Thermal |
| 70 | Busch (2016) | UWE-3 | Dock | Passive, monitoring | Functional, Thermal |
| 13 | [Eugene et al. (2016)](https://digitalcommons.usu.edu/smallsat/2016/TS13Education/4/) | Galassia | Dock | Passive, power conn., monitoring, std. conn. | Functional, Mission |
| 34 | [Gebara et al. (2016)](https://digitalcommons.usu.edu/smallsat/2016/TS8StudentComp/3/) | Prox-1 | Raw | — | Functional |
| 44 | [Spencer et al. (2016)](https://doi.org/10.2514/1.A33526) | Prox-1 | Raw | — | Functional |
| 26 | Askari et al. (2017) | Galassia | Dock | Passive, monitoring | Functional, Mission |
| 11 | Coelho (2017) | OPS-SAT | Raw, Dock | Passive, monitoring | Functional |
| 72 | Kshtriya (2017) | GHGSat-D | Raw | — | Functional |
| 64 | [Madzunkov et al. (2017)](http://hdl.handle.net/2014/49067) | S.A.M. | Raw | — | Functional |
| 49 | [Sabogal et al. (2017)](https://digitalcommons.usu.edu/smallsat/2017/all2017/163/) | SSIVP | Dock | Active, power conn., monitoring, std. conn. | Functional |
| 40 | Schummer (2017) | MOVE-II | Bridge | Passive, monitoring | Functional |
| 47 | Svatos (2017) | NORSAT-2 | Raw | — | Functional |
| 66 | Michael Chapman (2018) | BRITE | Raw | — | Functional, Mission |
| 20 | Gruber (2018) | MIST | Bridge | Passive, switches, power conn., monitoring | Functional |
| 12 | [Haber et al. (2018)](https://digitalcommons.usu.edu/smallsat/2018/all2018/269/) | QUBE | Dock | Passive, switches, power conn., monitoring, std. conn. | Functional |
| 31 | [Kepko et al. (2018)](https://digitalcommons.usu.edu/smallsat/2018/all2018/250/) | Dellingr | Bridge | Passive, monitoring | Functional |
| 39 | Langer (2018) | MOVE-II | Bridge | Passive, switches, monitoring | Functional |
| 87 | Macedo (2018) | ISTSat-1 | Modular | Passive, switches, power conn., monitoring | Functional |
| 42 | [Nogales et al. (2018)](https://digitalcommons.usu.edu/smallsat/2018/all2018/434/) | MakerSat-1 | Raw | — | — |
| 43 | Radu et al. (2018) | Delfi-PQ-1 | Dock | Active, switches, power conn., monitoring, std. conn. | Functional |
| 74 | [Asquier et al. (2019)](https://digitalcommons.usu.edu/smallsat/2019/all2019/77/) | CHEOPS | Raw | — | Functional |
| 67 | Barra (2019) | MIST | Bridge | Passive, switches, power conn., monitoring | Functional |
| 55 | [Alan Cassell et al. (2019)](https://doi.org/10.2514/6.2019-2896) | Nano-ADEPT | Raw | — | Functional |
| 69 | Hessinger (2019) | OPS-SAT | Raw, Dock | Passive, monitoring | Functional |
| 14 | Jain (2019) | DESCENT | Raw | — | Functional |
| 73 | Marquis (2019) | SFL missions | Raw | — | Functional |
| 7 | [Monteiro et al. (2019)](https://doi.org/10.3390/aerospace6120131) | ISTSat-1 | Modular | Passive, switches, power conn., monitoring | Functional, EMC |
| 41 | [Obata et al. (2019)](https://digitalcommons.usu.edu/smallsat/2019/all2019/91/) | CSSARSC | Raw | — | Functional |
| 79 | [Sternberg et al. (2019)](https://doi.org/10.1109/AERO.2019.8741816) | MarCO | Raw | — | Functional, Mission |
| 46 | [Taylor et al. (2019)](https://doi.org/10.1109/AERO.2019.8741738) | POINTR | Raw | — | Functional |
| 25 | [Turtogtokh Tumenjargal et al. (2019)](https://doi.org/10.1016/j.actaastro.2019.04.047) | BIRDS-3 | Dock | Active, monitoring, CPLD | Functional |
| 60 | Zanola (2019) | ESA-Prop | Dock | Passive, monitoring | Functional |
| 75 | Bätz (2020) | Flying Laptop | Raw | — | Functional |
| 36 | [Campbell et al. (2020)](https://digitalcommons.usu.edu/smallsat/2020/all2020/45/) | MakerSat-1 | Raw | — | — |
| 38 | Cheremetiev (2020) | Foresail-1 | Modular | Passive, power conn., monitoring | Functional |
| 45 | [Obata et al. (2020)](https://doi.org/10.1109/IGARSS39084.2020.9323284) | CSSARSC | Raw | — | Functional |
| 19 | Filip (2021) | VST104 | Dock | Active, sensors, switches, power conn., monitoring, std. conn. | Functional |
| 6 | [He et al. (2021)](\urlhttps://digitalcommons.usu.edu/smallsat/2021/all2021/282/) | CubeSat with a Raspberry Pi Zero | Raw | — | Functional |
| 54 | [Heimerl et al. (2021)](https://digitalcommons.usu.edu/smallsat/2021/all2021/240/) | MOCI | Dock | Passive, monitoring | Functional |
| 29 | [Kolhof et al. (2021)](https://digitalcommons.usu.edu/smallsat/2021/all2021/21/) | GT-1 | Raw | — | Functional |
| 22 | [Maeve Doyle et al. (2021)](https://doi.org/10.1117/12.2600305) | EIRSAT-1 | Dock | Passive, monitoring | Functional, Mission |
| 10 | Mahanti (2021) | BA CubeSat | Raw | — | Functional |
| 4 | Morea Font (2021) | 3CAT-4 | Dock | Passive, monitoring | Functional |
| 63 | [Perryman et al. (2021)](https://digitalcommons.usu.edu/smallsat/2021/all2021/241/) | CASPR | Dock | Active, power conn., monitoring, std. conn. | Functional |
| 5 | [Praks et al. (2021)](https://doi.org/10.1016/j.actaastro.2020.11.042) | Aalto-1 | Dock | Passive, switches, power conn., monitoring | Functional |
| 1 | [Walsh et al. (2021)](https://doi.org/10.3390/aerospace8090254) | EIRSAT-1 | Dock | Passive, monitoring | Functional, Mission |
