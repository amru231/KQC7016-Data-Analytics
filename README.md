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
Perform EDA on the Energy dataset and produce meaningful visualisations.

- [`lab2/Lab2.py`](lab2/Lab2.py) — EDA script
- [`lab2/Energy.csv`](lab2/Energy.csv) — Dataset
- [`report/lab2_report.md`](report/lab2_report.md) — Lab report

**Dataset features:** Timestamp, Temperature, Humidity, SquareFootage, Occupancy, HVACUsage, LightingUsage, RenewableEnergy, DayOfWeek, Holiday, EnergyConsumption

---

### Lab 3 — ANOVA
Demonstrate an ANOVA test on the Energy dataset, with justification for variable selection.

- [`lab3/Lab3.py`](lab3/Lab3.py) — ANOVA script
- [`lab3/Energy.csv`](lab3/Energy.csv) — Dataset
- [`report/lab3_report.md`](report/lab3_report.md) — Lab report

---

## Dataset

The `Energy.csv` dataset contains hourly energy consumption readings for a building, with the following features:

| Feature | Description |
|---|---|
| Timestamp | Date and time of reading |
| Temperature | Ambient temperature (°C) |
| Humidity | Relative humidity (%) |
| SquareFootage | Building area (sq ft) |
| Occupancy | Number of occupants |
| HVACUsage | HVAC system energy draw |
| LightingUsage | Lighting energy draw |
| RenewableEnergy | Renewable energy contribution |
| DayOfWeek | Day of the week |
| Holiday | Whether it is a public holiday |
| EnergyConsumption | Total energy consumption (target variable) |

---

## Tools and Libraries

- Python 3
- `requests`, `beautifulsoup4` — web scraping
- `pandas`, `matplotlib`, `seaborn` — EDA and visualisation
- `scipy`, `statsmodels` — statistical testing (ANOVA)
