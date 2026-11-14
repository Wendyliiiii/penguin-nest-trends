
# Long-Term Changes in Adélie Penguin Nest Counts at Cape Bird South (1984–2024)
**Authors:** Melody Qu and Wendy Li

## Project Overview
This project examines changes in Adélie penguin nest counts at Cape Bird South, Antarctica, from 1984 to 2024. The analysis explores long-term trends, differences between two time periods, and the largest year-to-year changes in nest counts.

## Research Questions
1. What is the overall trend in nest counts from 1984 to 2024?
2. Are the trends different between 1984–2003 and 2004–2024?
3. Which consecutive years had the biggest increase and decrease in nest counts?

## Dataset
The dataset comes from the Mapping Application for Penguin Populations and Projected Dynamics (MAPPPD), Version 5.0.
- Dataset website: https://www.penguinmap.com/mapppd/
- Download link: https://www.penguinmap.com/mapppd/DownloadAll
- Original dataset: 5,487 rows and 15 columns
- Filtered dataset: 40 breeding-season observations
- Study location: Cape Bird South, Antarctica
- Species: Adélie penguin
- Count type: Nests
- Observation method: Aerial surveys
- Study period: 1984–2024

There is no observation for 2020. The original CSV file is not included in this repository.

## Tools and Libraries
- Python
- pandas
- seaborn
- matplotlib
- SciPy

## Running the Code
### 1. Download the Dataset
Download the MAPPPD Version 5.0 dataset and place `AllCounts_V_5_0.csv` in the project folder.
### 2. Install Required Libraries
```bash
python -m pip install pandas seaborn matplotlib scipy
```
### 3. Run the Analysis
```bash
python eda.py
```
### 4. Run the Tests
```bash
python test_eda.py
```

## Visualizations
The analysis generates two figures:
- `penguin_trend.png`: Annual nest counts from 1984 to 2024.
- `penguin_distribution.png`: Distribution of nest counts across breeding seasons.

## Statistical Methods
The analysis uses Kendall's tau to examine monotonic associations between breeding season and nest count. Theil–Sen slope estimates are used to describe changes in nest counts over time. Lag-one correlations are also calculated to investigate temporal dependence between consecutive breeding seasons. Because annual observations may not be independent, conventional p-values and confidence intervals are interpreted cautiously.

## Testing
The `test_eda.py` file includes tests for:
- Correct year-to-year change calculations.
- Missing breeding seasons.
- Unsorted observations.

## Project Status
Exploratory data analysis (EDA) for CSE 163, Autumn 2026.