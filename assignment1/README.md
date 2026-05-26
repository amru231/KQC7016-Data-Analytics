# Assignment 1 — Exploratory Data Analysis & Hypothesis Testing

**Course:** KQC7016 Data Analytics, Semester 2, 2025/2026
**Theme:** 7 — Autonomous Driving
**Group:** Muhammad Amru Bin Mohamad Sharis (S2116804) · Nor Shahadah Fitrah Binti Ramani (25073210)
**Instructor:** Associate Prof. Ir. Dr. Chow Chee Onn

---

## Overview

We apply Exploratory Data Analysis (EDA) and statistical hypothesis testing in Python to real-world
US autonomous-vehicle crash reports. The guiding research question is:

> **How do incident patterns and injury outcomes differ between vehicles operating with ADS
> (Level 3+) versus ADAS (Level 1–2) automation in the United States?**

Two pre-specified hypotheses are tested:

- **H1** — The distribution of roadway types differs between ADS and ADAS incidents (chi-square test of independence).
- **H2** — Injury severity differs between ADS and ADAS incidents (Mann-Whitney U, with a stratified
  sensitivity analysis to control for the operational-domain confound).

The full write-up is in [`../report/assignment1_report.md`](../report/assignment1_report.md).

## Dataset

**NHTSA Standing General Order 2021-01** — *Incident Reports of Crashes Involving Vehicles Equipped
with ADS or Level 2 ADAS* ([source](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting)).
Four CSVs (current + prior templates) covering 2019–2026, each crash a wide record of 116–137 columns.

After cleaning the working dataset is **6,450 unique incident reports** (latest report version per
incident), with ADS / ADAS / Unknown counts of 2,670 / 3,549 / 231. Raw files are in
[`dataset/NHTSA_SGA_AV/`](dataset/NHTSA_SGA_AV/); the cleaned output is
[`notebooks/data/cleaned.csv`](notebooks/data/cleaned.csv).

## Methodology

Implemented across three Jupyter notebooks (run in order):

| Notebook | Purpose |
|----------|---------|
| [`notebooks/01_clean.ipynb`](notebooks/01_clean.ipynb) | Encoding-tolerant load, schema reconciliation across the 116/137-column templates, de-duplication by report version, make normalisation, date parsing, weather collapse, ordinal severity encoding |
| [`notebooks/02_eda.ipynb`](notebooks/02_eda.ipynb) | EDA and the 13 figures in [`notebooks/plots/`](notebooks/plots/) — fleet composition, trends, roadway×system, severity×system, speed, correlations |
| [`notebooks/03_stats.ipynb`](notebooks/03_stats.ipynb) | H1 chi-square (+ Cramér's V, standardised residuals) and H2 Mann-Whitney U (+ rank-biserial effect size, stratified by roadway) |

**Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`.

## Key Findings

- **ADS and ADAS occupy near-non-overlapping road environments.** ADAS incidents concentrate on
  highways/freeways; ADS incidents concentrate on streets, intersections, and parking lots.
  Chi-square: χ²(4) = 2,442, p < 0.001, Cramér's V = 0.682 (large).
- **Injury severity is consistently lower for ADS than ADAS.** Mann-Whitney U p ≈ 5×10⁻¹¹¹,
  rank-biserial r = +0.408 (medium), and the gap **persists in every roadway stratum**
  (p < 0.001 each) — so it is not purely a highway-speed artefact.
- **Limitations:** severe reporting asymmetry (86% of ADAS reports list "Unknown" severity), no
  exposure (miles-driven) denominator, and schema-coverage gaps. Findings are descriptive
  associations, not causal claims.

## Folder Structure

```text
assignment1/
├── README.md            # This file
├── dataset/             # Raw NHTSA SGO CSVs + data-element definitions
├── notebooks/           # 01_clean, 02_eda, 03_stats + data/ and plots/ outputs
├── reference/           # Cited papers (PDF) and report figures
└── instruction/         # Assignment brief (KQC7016_20252026S2_Asgn1.pdf)
```

Full report: [`../report/assignment1_report.md`](../report/assignment1_report.md).
