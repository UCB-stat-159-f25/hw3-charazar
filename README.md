# LIGO Gravitational Wave Detection Tutorial

**Statistics 159/259, Fall 2025**  
**Authors:** LIGO Scientific Collaboration (LSC) and Char Tomlinson
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-charazar.git/HEAD)

## About

This project analyzes gravitational wave data from LIGO's detection of GW150914 - the first observation of gravitational waves from merging black holes. The code processes signals from LIGO's Hanford and Livingston detectors and creates visualizations and audio files of the gravitational wave event.


## Repository Structure

- `data/` - LIGO detector data files
- `figures/` - Generated plots
- `audio/` - Audio files of gravitational waves
- `ligotools/` - Python package with analysis tools
- `LOSC_Event_tutorial.ipynb` - Main analysis notebook

## Running Tests
```bash
pytest ligotools
```

## Building the Website
```bash
make html
```

View the deployed site at: https://github.com/UCB-stat-159-f25/hw3-charazar.git 

## Makefile Commands

- `make env` - Create/update conda environment
- `make html` - Build MyST website
- `make clean` - Remove generated files

## Data Source

Data from the [LIGO Open Science Center](https://www.gw-openscience.org/) for the GW150914 event detected on September 14, 2015.

## Requirements

- Python >= 3.9
- See `environment.yml` for full dependencies

---

**Course:** Statistics 159/259, Fall 2025
