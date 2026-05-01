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

- [`lab2/lab2.py`](lab2/lab2.py) — EDA script
- [`dataset/WorldEnergy.csv`](dataset/WorldEnergy.csv) — Dataset
- [`report/lab2_report.md`](report/lab2_report.md) — Lab report

---

### Lab 3 — ANOVA
Demonstrate an ANOVA test on the World Energy dataset, with justification for variable selection.

- [`lab3/lab3.py`](lab3/lab3.py) — ANOVA script
- [`dataset/WorldEnergy.csv`](dataset/WorldEnergy.csv) — Dataset
- [`report/lab3_report.md`](report/lab3_report.md) — Lab report

---

## Assignments

### Assignment 1 — Exploratory Data Analytics
Apply Exploratory Data Analysis (EDA) and statistical hypothesis testing to a real-world dataset using Python.

- [`assignment1/KQC7016_20252026S2_Asgn1.pdf`](assignment1/KQC7016_20252026S2_Asgn1.pdf) — Assignment brief

**Main requirements:** Jupyter Notebook and brief report, maximum 10 pages.

**Report format:** Cover Page, Introduction, Description of Datasets, Exploratory Data Analysis, Statistical Analysis, Conclusion, References.

---

### Assignment 2 — AI for Medicine
Apply advanced data analytics techniques to a medical or healthcare-related problem using an end-to-end data analysis pipeline.

- [`assignment2/KQC7016_20252026S2_Asgn2.pdf`](assignment2/KQC7016_20252026S2_Asgn2.pdf) — Assignment brief

**Main requirements:** Technical report, maximum 15 pages, GitHub link in report, and 5-minute recorded presentation.

**Methods requirement:** Use at least two different analytics methods, such as regression, clustering, association rule mining, or classification.

**Report format:** Cover Page, Abstract, Introduction, Problem Definition, Data Description & EDA, Proposed AI-based Solution Concept, Results & Discussion, Conclusion, References.

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

## Tools and Libraries

- Python 3
- `requests`, `beautifulsoup4` — web scraping
- `pandas`, `matplotlib`, `seaborn` — EDA and visualisation
- `scipy`, `statsmodels` — statistical testing (ANOVA)
