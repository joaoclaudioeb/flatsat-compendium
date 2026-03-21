<h1 align="center">
    COMPENDIUM: FLATSAT PLATFORMS, TESTS AND MORE
</h1>

This repository compiles experimental data, simulation results, research assets, and systematic mappings related to FlatSat platform development. Each release receives a DOI via Zenodo for permanent citation in publications.

---

## Repo. structure  

```bash
flatsat-compendium/
├── platform/
│   ├── flatsat-platform2-firmware/
│   └── flatsat-platform2-hardware/
│
├── experiments/
│   ├── experiment-yyyy-mm/
│   │   ├── figures/
│   │   ├── README
│   │   ├── (...)/
│   │   └── embedded-sensors-data/raw-data
│   │       └── read-sensors.sqlite3
│   │
│   (...)
├── README
├── research/
└── (...)/

## Licenses

Unless otherwise noted, original files in this repository are licensed under:

- Firmware: GPL-2.0
- Hardware: CERN Open Hardware License v2.0

>[!CAUTION]
>Files originating from AMD/Xilinx tools, PetaLinux, Yocto, Linux, U-Boot, Avnet or other third parties remain under their respective licenses and are not relicensed by this project.