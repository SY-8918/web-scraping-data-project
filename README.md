# Web Scraping Data Project

Python-based web scraping project designed to collect, structure, and analyze online data automatically.

## Project Overview

This project extracts book information from an online bookstore dataset and transforms it into structured data for analysis and visualization.

The project includes:

* data extraction
* cleaning and conversion
* availability analysis
* price analysis
* rating analysis
* visual reporting

## Technologies

* Python
* BeautifulSoup
* Requests
* Pandas
* Matplotlib

## Files

* `mod_main.py` → main scraping workflow
* `Convert.py` → data cleaning and transformation
* `books_dataset.csv` → generated dataset
* `Histogramme des prix.py` → price distribution chart
* `Graphique du nombre de livres par rating.py` → books by rating chart

## Visualizations

### Price Distribution

![Price Histogram](images/histogramme_prix.png)

### Number of Books by Rating

![Books by Rating](images/livres_par_rating.png)

## Key Insights

* Most books are concentrated in lower and mid price ranges.
* Rating distribution helps identify the most common product quality levels.
* The dataset can support price monitoring and product trend analysis.

## Business Value

This type of scraping workflow can be used for:

* competitor monitoring
* market research
* price tracking
* product availability analysis
