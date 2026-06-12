# Assignment 2 — Explainable Maternal Health Risk Prediction

**Course:** KQC7016 Data Analytics, Semester 2, 2025/2026
**Theme:** AI for Medicine
**Group:** Muhammad Amru Bin Mohamad Sharis (S2116804) · Nor Shahadah Fitrah Binti Ramani (25073210)
**Instructor:** Associate Prof. Ir. Dr. Chow Chee Onn

---

## Overview

We build an **explainable** maternal-health risk decision-support pipeline on IoT-collected
vital-sign data. Most published models on this dataset chase accuracy and give little
patient-level reasoning; clinicians in low-resource, IoT-monitored settings need the *why*.
The guiding research question is:

> **How can we predict maternal health risk from vital-sign data while giving interpretable,
> patient-specific explanations for decision support?**

The project combines **two analytics methods** (satisfying the ≥2-methods requirement):

- **Classification** — predict `low` / `mid` / `high` risk from six vital signs.
- **Association Rule Mining** — surface interpretable vital-sign → risk patterns.

On top, an explainability layer (SHAP + matched rules) and a **small language model (SLM)**
narrative module turn structured evidence into a readable clinical explanation (explanation
only — the SLM does **not** predict).

The full write-up is in [`notes/report_draft.md`](notes/report_draft.md).

## Dataset

**UCI Maternal Health Risk** (Ahmed, 2020) — IoT-collected vitals from rural Bangladesh
hospitals/clinics ([source](https://doi.org/10.24432/C5DP5D)). Raw file in
[`dataset/`](dataset/).

- 1,014 rows · 6 features (Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate) · 3-class target.
- Class balance: low 406 / mid 336 / high 272 (mild imbalance).
- **0 nulls**, but **562 exact duplicate rows (55%)** → only **452 unique** records.
  Duplicates are removed **before** the train/test split to prevent leakage; a sensitivity
  analysis on the full 1,014-row set quantifies the inflation effect.
- 2 impossible records (`HeartRate = 7`, sensor error) are fixed in preprocessing.

## Methodology

Implemented across six Jupyter notebooks (run in order):

| Notebook | Purpose |
|----------|---------|
| `notebooks/01_preprocess.ipynb` | Load, duplicate audit, dedup-before-split, HeartRate=7 outlier fix, target encoding, stratified train/test split + full-set sensitivity copy |
| `notebooks/02_eda.ipynb` | Class & feature distributions, correlation heatmap, per-class boxplots (BS / BP / Age), duplicate & outlier audit → figures in `notebooks/plots/` |
| `notebooks/03_classification.ipynb` | Decision Tree, Random Forest (primary), XGBoost; macro-F1 + high-risk recall + confusion matrix; stratified CV |
| `notebooks/04_association_rules.ipynb` | Clinically-justified discretization, Apriori/FP-Growth, rules ranked by support/confidence/lift |
| `notebooks/05_explainability.ipynb` | SHAP values + feature importance + patient→rule matching |
| `notebooks/06_slm_narrative.ipynb` | Structured evidence → SLM clinical narrative (Llama-3.2-1B/3B, Qwen3-1.7B); manual rubric eval |

**Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`,
`mlxtend` (ARM), `shap`, plus `transformers` / `llama-cpp-python` for the SLM module.
See [`requirements.txt`](requirements.txt).

## Evaluation Priority

Metrics in priority order: **Macro-F1 · High-risk recall · Confusion matrix**, with accuracy
secondary. Rationale: missing a high-risk patient is more dangerous than over-flagging a
low-risk one, so recall on the high-risk class is clinically weighted above raw accuracy.

## Folder Structure

```text
assignment2/
├── README.md            # This file
├── dataset/             # UCI Maternal Health Risk CSV
├── notebooks/           # 01–06 notebooks + data/ and plots/ outputs
├── notes/               # report_draft.md (working report)
├── paper/               # Cited papers (PDF)
└── instruction/         # Assignment brief (KQC7016_20252026S2_Asgn2.pdf)
```

## Environment

Python 3, `python3` interpreter. SLM module uses an RTX 3050 Laptop GPU (4 GB VRAM, CUDA);
the 3B model runs 4-bit quantized (GGUF). Install with:

```bash
pip install -r requirements.txt
```
