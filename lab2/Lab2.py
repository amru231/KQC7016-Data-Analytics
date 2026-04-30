import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WorldEnergy.csv")

print(df.head())
print(df.info())
print(df.describe())

# Graph 1
plt.figure()
sns.histplot(df.select_dtypes(include='number').iloc[:,0], kde=True)
plt.title("Distribution")
plt.show()

# Graph 2
plt.figure(figsize=(10, 6))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# A++ grade
plt.figure(figsize=(12,8))

corr = df.select_dtypes(include='number').iloc[:, :15].corr()

sns.heatmap(
    corr,
    cmap="coolwarm",
    linewidths=0.3,
    cbar=True
)

plt.title("Correlation Heatmap (Top 15 Variables)")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

plt.show()