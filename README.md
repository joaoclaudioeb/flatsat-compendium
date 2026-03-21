<h1 align="center">
    COMPENDIUM: FLATSAT PLATFORMS, TESTS AND MORE
</h1>

This repository collects resources from the development and validation of the FlatSat 2.0 platform, an open-source hardware and software project for CubeSat verification. It includes design files, firmware, software, and experimental data from validation campaigns.

The platform features embedded current and temperature sensors, a reconfigurable system-on-module running Linux, and support for hardware- and software-based fault injection. These capabilities enable unified telemetry logging, subsystem emulation, and on-orbit scenario simulation without external instrumentation.

Future additions may include daughterboards for extended emulation, results from new test campaigns, and contributions from other missions that build upon or adapt the platform.

<p align="center">
    <img src="https://github.com/joaoclaudioeb/flatsat-compendium/blob/main/experiments/experiment-2025-09/figures/flatsat-edc-test.jpg?raw=true" width="400">
    <img src="https://github.com/joaoclaudioeb/flatsat-compendium/blob/main/experiments/experiment-2026-01/figures/flatsat-ltc-test.jpg?raw=true" width="400">
</p>

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
```

## Licenses

Unless otherwise noted, original files in this repository are licensed under:

- Firmware: GPL-2.0
- Hardware: CERN Open Hardware License v2.0

>[!CAUTION]
>Files originating from AMD/Xilinx tools, PetaLinux, Yocto, Linux, U-Boot, Avnet or other third parties remain under their respective licenses and are not relicensed by this project.