"""
KQC7016 Data Analytics — Lab 3: ANOVA
Group: Muhammad Amru (S2116804) & Nor Shahadah Fitrah (25073210)

Dataset : WorldEnergy.csv (Our World in Data)
Objective: Demonstrate One-Way and Two-Way ANOVA on world energy data.

Research Questions:
  Q1 (One-Way) : Does the mean renewable energy share differ significantly
                 across year groups (decades)?
  Q2 (Two-Way) : Do year group AND fossil dominance category, including their
                 interaction, significantly affect renewable energy share?

Columns chosen:
  Dependent   : renewables_share_energy  (% of primary energy from renewables)
  Factor 1    : year_group               (decade bins: 1990s, 2000s, 2010s, 2020s)
  Factor 2    : fossil_dominance         (High / Low — split at dataset median)
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')          
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ── Output directory ──────────────────────────────────────────────────────────
PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

# ── 1. Load & clean data ──────────────────────────────────────────────────────
print("=" * 65)
print("KQC7016 Lab 3 — ANOVA on World Energy Dataset")
print("=" * 65)

df_raw = pd.read_csv(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 '../dataset/WorldEnergy.csv')
)

print(f"\nRaw dataset shape : {df_raw.shape}")

# Keep only actual countries (rows with an ISO code) to exclude regional aggregates
df = df_raw[df_raw['iso_code'].notna()].copy()

# Focus on 1990–2024 where renewable share data is reasonably populated
df = df[(df['year'] >= 1990) & (df['year'] <= 2024)]

# Drop rows missing the target variable
df = df.dropna(subset=['renewables_share_energy', 'fossil_share_energy'])

print(f"Working dataset    : {len(df)} rows, {df['country'].nunique()} countries, "
      f"years {int(df['year'].min())}–{int(df['year'].max())}")

# ── 2. Create categorical factors ─────────────────────────────────────────────
# Factor 1 — Year Group (decade bins)
bins   = [1989, 1999, 2009, 2019, 2024]
labels = ['1990–1999', '2000–2009', '2010–2019', '2020–2024']
df['year_group'] = pd.cut(df['year'], bins=bins, labels=labels)

# Factor 2 — Fossil Dominance (above / below dataset median)
median_fossil = df['fossil_share_energy'].median()
df['fossil_dominance'] = np.where(
    df['fossil_share_energy'] > median_fossil, 'High Fossil', 'Low Fossil'
)

print(f"\nMedian fossil share used as split: {median_fossil:.1f}%")
print("\nSample counts per year_group:")
print(df['year_group'].value_counts().sort_index().to_string())
print("\nSample counts per fossil_dominance:")
print(df['fossil_dominance'].value_counts().to_string())

# ── 3. Descriptive statistics ──────────────────────────────────────────────────
print("\n--- Descriptive Statistics: renewables_share_energy ---")
desc = df.groupby('year_group', observed=True)['renewables_share_energy'].describe()
print(desc.round(2).to_string())

# ── 4. Visualisations ─────────────────────────────────────────────────────────
sns.set_theme(style='whitegrid', palette='muted')

# Plot 1 — Boxplot: renewables by year_group
fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=df, x='year_group', y='renewables_share_energy',
            order=labels, ax=ax, hue='year_group', palette='Blues', legend=False)
ax.set_title('Renewable Energy Share by Year Group', fontsize=14, fontweight='bold')
ax.set_xlabel('Year Group')
ax.set_ylabel('Renewables Share of Primary Energy (%)')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '01_boxplot_renewables_by_yeargroup.png'), dpi=150)
plt.close(fig)
print("\n[Saved] 01_boxplot_renewables_by_yeargroup.png")

# Plot 2 — Boxplot: renewables by fossil_dominance
fig, ax = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='fossil_dominance', y='renewables_share_energy',
            ax=ax, hue='fossil_dominance', palette='Set2', legend=False)
ax.set_title('Renewable Energy Share by Fossil Dominance', fontsize=14, fontweight='bold')
ax.set_xlabel('Fossil Dominance Category')
ax.set_ylabel('Renewables Share of Primary Energy (%)')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '02_boxplot_renewables_by_fossil.png'), dpi=150)
plt.close(fig)
print("[Saved] 02_boxplot_renewables_by_fossil.png")

# Plot 3 — Interaction plot: year_group × fossil_dominance
fig, ax = plt.subplots(figsize=(9, 5))
sns.pointplot(data=df, x='year_group', y='renewables_share_energy',
              hue='fossil_dominance', order=labels,
              errorbar='sd', dodge=True, markers=['o', 's'], capsize=0.1,
              palette='Set1', ax=ax)
ax.set_title('Interaction: Year Group × Fossil Dominance\non Renewable Energy Share',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Year Group')
ax.set_ylabel('Renewables Share of Primary Energy (%)')
ax.legend(title='Fossil Dominance')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '03_interaction_plot.png'), dpi=150)
plt.close(fig)
print("[Saved] 03_interaction_plot.png")

# Plot 4 — Distribution of renewables_share_energy (overall)
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df['renewables_share_energy'], bins=40, kde=True, ax=ax, color='steelblue')
ax.set_title('Distribution of Renewable Energy Share', fontsize=13, fontweight='bold')
ax.set_xlabel('Renewables Share of Primary Energy (%)')
ax.set_ylabel('Count')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '04_distribution_renewables.png'), dpi=150)
plt.close(fig)
print("[Saved] 04_distribution_renewables.png")

# ── 5. One-Way ANOVA ──────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("ONE-WAY ANOVA")
print("H0: Mean renewables_share_energy is equal across all year groups")
print("H1: At least one year group mean is significantly different")
print("=" * 65)

# Drop rows where year_group is NaN (boundary years)
df_anova = df.dropna(subset=['year_group']).copy()
df_anova['year_group'] = df_anova['year_group'].astype(str)

model_1way = ols('renewables_share_energy ~ C(year_group)', data=df_anova).fit()
anova_1way = sm.stats.anova_lm(model_1way, typ=2)
print("\nOne-Way ANOVA Table:")
print(anova_1way.round(4).to_string())

p_1way = anova_1way.loc['C(year_group)', 'PR(>F)']
f_1way = anova_1way.loc['C(year_group)', 'F']
print(f"\nF-statistic : {f_1way:.4f}")
print(f"p-value     : {p_1way:.6f}")
if p_1way < 0.05:
    print("Result      : SIGNIFICANT — reject H0 (p < 0.05)")
    print("             Year group significantly affects renewable energy share.")
else:
    print("Result      : NOT significant — fail to reject H0 (p >= 0.05)")

# ── 6. Post-hoc Tukey HSD ─────────────────────────────────────────────────────
print("\n--- Post-hoc: Tukey HSD (pairwise year group comparisons) ---")
tukey = pairwise_tukeyhsd(
    df_anova['renewables_share_energy'],
    df_anova['year_group'],
    alpha=0.05
)
print(tukey)

# Plot 5 — Tukey HSD result
fig = tukey.plot_simultaneous(figsize=(9, 5))
plt.title('Tukey HSD — 95% Confidence Intervals by Year Group', fontweight='bold')
plt.xlabel('Mean Difference in Renewables Share (%)')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '05_tukey_hsd.png'), dpi=150)
plt.close(fig)
print("[Saved] 05_tukey_hsd.png")

# ── 7. Two-Way ANOVA ──────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("TWO-WAY ANOVA")
print("Factors : year_group  ×  fossil_dominance")
print("H0_A: No main effect of year group")
print("H0_B: No main effect of fossil dominance")
print("H0_AB: No interaction effect between year group and fossil dominance")
print("=" * 65)

model_2way = ols(
    'renewables_share_energy ~ C(year_group) * C(fossil_dominance)',
    data=df_anova
).fit()
anova_2way = sm.stats.anova_lm(model_2way, typ=2)
print("\nTwo-Way ANOVA Table:")
print(anova_2way.round(4).to_string())

for term, label in [
    ('C(year_group)', 'Year Group (main effect)'),
    ('C(fossil_dominance)', 'Fossil Dominance (main effect)'),
    ('C(year_group):C(fossil_dominance)', 'Interaction'),
]:
    p = anova_2way.loc[term, 'PR(>F)']
    f = anova_2way.loc[term, 'F']
    sig = "SIGNIFICANT" if p < 0.05 else "not significant"
    print(f"\n  {label}: F={f:.4f}, p={p:.6f} → {sig}")

# ── 8. Assumption Checks ──────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("ASSUMPTION CHECKS")
print("=" * 65)

# 8a. Normality of residuals — Shapiro-Wilk
# Use a random sample ≤ 5000 (Shapiro-Wilk limit)
residuals = model_2way.resid
rng = np.random.default_rng(42)
sample_resid = rng.choice(residuals, size=min(5000, len(residuals)), replace=False)
shapiro_stat, shapiro_p = stats.shapiro(sample_resid)
print(f"\nShapiro-Wilk Test (normality of residuals, n={len(sample_resid)}):")
print(f"  W = {shapiro_stat:.6f},  p = {shapiro_p:.6f}")
if shapiro_p > 0.05:
    print("  → Residuals are normally distributed (p > 0.05)")
else:
    print("  → Residuals deviate from normality (p < 0.05)")
    print("     Note: ANOVA is robust to mild non-normality with large samples.")

# 8b. Homogeneity of Variance — Levene's Test
groups_for_levene = [
    group['renewables_share_energy'].values
    for _, group in df_anova.groupby('year_group')
]
levene_stat, levene_p = stats.levene(*groups_for_levene)
print(f"\nLevene's Test (homogeneity of variance across year groups):")
print(f"  W = {levene_stat:.6f},  p = {levene_p:.6f}")
if levene_p > 0.05:
    print("  → Equal variances assumption holds (p > 0.05)")
else:
    print("  → Variances are unequal (p < 0.05)")
    print("     Note: ANOVA is somewhat robust; Welch's correction can be applied.")

# Plot 6 — Q-Q plot of residuals
fig, ax = plt.subplots(figsize=(6, 5))
sm.qqplot(residuals, line='s', ax=ax, alpha=0.4, markersize=2)
ax.set_title("Q-Q Plot of Residuals (Two-Way ANOVA)", fontsize=13, fontweight='bold')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '06_qq_plot_residuals.png'), dpi=150)
plt.close(fig)
print("\n[Saved] 06_qq_plot_residuals.png")

# Plot 7 — Residuals vs Fitted
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(model_2way.fittedvalues, residuals, alpha=0.3, s=5, color='steelblue')
ax.axhline(0, color='red', linewidth=1, linestyle='--')
ax.set_title('Residuals vs Fitted Values', fontsize=13, fontweight='bold')
ax.set_xlabel('Fitted Values')
ax.set_ylabel('Residuals')
plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, '07_residuals_vs_fitted.png'), dpi=150)
plt.close(fig)
print("[Saved] 07_residuals_vs_fitted.png")

print("\n" + "=" * 65)
print("Lab 3 complete. All plots saved to:", PLOTS_DIR)
print("=" * 65)
