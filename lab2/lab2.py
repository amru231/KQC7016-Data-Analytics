import os
os.makedirs("plots", exist_ok=True)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WorldEnergy.csv")

print(df.head())
print(df.info())
print(df.describe())

# -----------------------
# Graph 1: Histogram
# -----------------------
plt.figure()

num_col = df.select_dtypes(include='number').columns[0]
sns.histplot(df[num_col], kde=True)

plt.title(f"Distribution of {num_col}")
plt.xlabel(num_col)
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("plots/histogram.png", dpi=300)
plt.show()


# -----------------------
# Graph 2: Full Heatmap
# -----------------------
plt.figure(figsize=(16, 12))

corr_full = df.select_dtypes(include='number').corr()

sns.heatmap(
    corr_full,
    cmap="coolwarm",
    linewidths=0.2,
    cbar=True
)

plt.title("Full Correlation Heatmap")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()

plt.savefig("plots/full_heatmap.png", dpi=300)
plt.show()


# -----------------------
# Graph 3: Top 15 Heatmap
# -----------------------
plt.figure(figsize=(12, 8))

corr_top15 = df.select_dtypes(include='number').iloc[:, :15].corr()

sns.heatmap(
    corr_top15,
    cmap="coolwarm",
    linewidths=0.3,
    cbar=True
)

plt.title("Correlation Heatmap (Top 15 Variables)")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

plt.savefig("plots/top15_heatmap.png", dpi=300)
plt.show()