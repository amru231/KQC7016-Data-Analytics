# KQC7016 Data Analytics

**Program:** Masters of Systems Engineering  
**Course:** KQC7016 Data Analytics SEM 2 25/26
**Instructor:** ASSOCIATE PROF. IR. DR. CHOW CHEE ONN

Group Members
1. Muhammad Amru Bin Mohamad Sharis (S2116804)
2. Nor Shahadah Fitrah Binti Ramani (25073210)

Labs are worth 5% carry mark each and are completed in groups of two.

---

## Labs

### Lab 1 — Web Scraping
Study and run a provided web scraping script, then modify it to scrape a different website.

- [`lab1/lab1.py`](lab1/lab1.py) — Original code: scrapes job listings from [realpython.github.io/fake-jobs](https://realpython.github.io/fake-jobs/)
- [`lab1/lab1_modified.py`](lab1/lab1_modified.py) — Modified code: scrapes quotes from [quotes.toscrape.com](https://quotes.toscrape.com/)
- [`report/lab1_report.md`](report/lab1_report.md) — Lab report

**Libraries used:** `requests`, `beautifulsoup4`

---

### Lab 2 — Exploratory Data Analysis (EDA)
Perform EDA on the World Energy dataset and produce meaningful visualisations.

- [`lab2/Lab2.py`](lab2/Lab2.py) — EDA script
- [`dataset/WorldEnergy.csv`](dataset/WorldEnergy.csv) — Dataset
- [`report/lab2_report.md`](report/lab2_report.md) — Lab report

---

### Lab 3 — ANOVA
Demonstrate an ANOVA test on the World Energy dataset, with justification for variable selection.

- [`lab3/Lab3.py`](lab3/Lab3.py) — ANOVA script
- [`dataset/WorldEnergy.csv`](dataset/WorldEnergy.csv) — Dataset
- [`report/lab3_report.md`](report/lab3_report.md) — Lab report

---

## Dataset

The `WorldEnergy.csv` dataset (located in `dataset/`) contains global energy statistics by country and year, sourced from Our World in Data. It covers production and consumption across all major energy types.

| Feature Group | Key Columns |
|---|---|
| Identifiers | `country`, `year`, `iso_code`, `population`, `gdp` |
| Primary Energy | `primary_energy_consumption`, `energy_per_capita`, `energy_per_gdp` |
| Fossil Fuels | `coal_consumption`, `oil_consumption`, `gas_consumption`, `fossil_fuel_consumption` |
| Renewables | `renewables_consumption`, `solar_consumption`, `wind_consumption`, `hydro_consumption`, `biofuel_consumption` |
| Low Carbon | `low_carbon_consumption`, `nuclear_consumption` |
| Electricity | `electricity_generation`, `electricity_demand`, `per_capita_electricity` |
| Emissions | `greenhouse_gas_emissions`, `carbon_intensity_elec` |
| Share Metrics | `renewables_share_energy`, `fossil_share_energy`, `low_carbon_share_elec`, etc. |

---

## Lecture Weeks

### Week 5 — EDA Visualization using Seaborn
Exploratory Data Analysis using Seaborn on a synthetic employee productivity dataset (300 employees across 5 departments).

- [`week5/EDA_Visualization_with_Seaborn.ipynb`](week5/EDA_Visualization_with_Seaborn.ipynb) — Seaborn visualization notebook
- [`week5/plot_interpretations.md`](week5/plot_interpretations.md) — Annotated interpretations for each plot
- [`week5/plots/`](week5/plots/) — Generated PNG plots (9 visualisations)
- [`week5/employee_productivity.csv`](week5/employee_productivity.csv) — Dataset

**Topics covered:** Univariate (histogram, boxplot, countplot), Bivariate (scatterplot, lineplot, barplot), Multivariate (pairplot, heatmap, violin plot)

**Key findings:** Salary follows a Normal distribution; no linear relationship between experience/age and salary; Work_Hours and Satisfaction_Level have a notable negative correlation (-0.47); overtime is associated with lower satisfaction levels.

---

## Tools and Libraries

- Python 3
- `requests`, `beautifulsoup4` — web scraping
- `pandas`, `matplotlib`, `seaborn` — EDA and visualisation
- `scipy`, `statsmodels` — statistical testing (ANOVA)
