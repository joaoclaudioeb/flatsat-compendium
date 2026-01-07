<h1 align="center">
    COMPENDIUM: FLATSAT PLATFORMS, TESTS AND MORE
</h1>

This repository compiles experimental data, simulation results, research assets, and systematic mappings related to FlatSat platform development. Each release receives a DOI via Zenodo for permanent citation in publications. TODO: we need to describe the licenses to be used here (each project already has one, and for data and etc. we could use another).

---

### Repo. structure  

```bash
flatsat-compendium/
├── platform/
│   ├── flatsat2-platform
│   │   ├── firmware/
│   │   └── hardware/
│   (...)
├── experiments/
│   ├── experiment-yyyy-mm/
│   │   ├── data/
│   │   ├── analysis/
│   │   ├── figures/
│   │   └── raw-data/
│   │       ├── sqlite-databases/
│   │       └── test-logs/
│   (...)
├── research/
└── simulations/
