# KQC7016 Data Analytics — Project Context

## Course
- **Course:** KQC7016 Data Analytics
- **Program:** Masters of Systems Engineering
- **Labs:** Group of two, submitted as a single zip: `KQC7016_Lab_TeamX.zip` or `.rar`
- **Each lab:** 5% carry mark

## Project Structure
```
data_analytics/
├── lab1/           # Lab 1 - Web Scraping
│   ├── lab1.py             # Original provided code (scrapes realpython fake-jobs)
│   └── lab1_modified.py    # Modified version (scrapes quotes.toscrape.com)
├── lab2/           # Lab 2 - EDA
│   └── Energy.csv          # World energy dataset
├── lab3/           # Lab 3 - ANOVA
│   └── Energy.csv          # World energy dataset
├── report/         # Lab reports go here
├── week6/          # Lecture materials (not graded, occasional help needed)
│   ├── Anova.ipynb
│   └── tensile_strength_data.csv
└── manual/
    └── KQC7016_Labs.pdf    # Lab manual
```

## Lab Requirements

### Lab 1 — Web Scraping (5%)
- Study and run `lab1.py`, explain each part with output screenshots
- Modify the code to scrape a different website (`lab1_modified.py`)
- Deliver: Lab Report 1 (with GitHub link)

### Lab 2 — EDA (5%)
- Write `Lab2.py` to perform EDA on `Energy.csv` and plot meaningful graphs
- In report: explain what type of data analytics project can be done with this dataset
- AI allowed for coding, not analysis
- Deliver: Lab Report 2 (with GitHub link)

### Lab 3 — ANOVA (5%)
- Write `Lab3.py` to demonstrate ANOVA test on `Energy.csv`
- In report: explain why the data/columns were chosen and provide discussion
- AI allowed for coding, not analysis
- Deliver: Lab Report 3 (with GitHub link)

## Working Notes
- Reports are drafted and finalized under `/report/`
- AI assistance is fine for coding AND interpretation/explanation of outputs; user will finalize analysis wording
- The `Energy.csv` dataset covers hourly energy consumption with features: Timestamp, Temperature, Humidity, SquareFootage, Occupancy, HVACUsage, LightingUsage, RenewableEnergy, DayOfWeek, Holiday, EnergyConsumption
