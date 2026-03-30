# Web Scraping Data Project

Python-based web scraping project designed to collect, structure, and analyze online data automatically.

## Project Overview

This project extracts book information from an online bookstore dataset and transforms it into structured data for analysis and visualization.

The project includes:

* Data extraction
* Cleaning and conversion
* Availability analysis
* Price analysis
* Rating analysis
* Visual reporting

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

* Most books are concentrated in lower price ranges.
* Higher ratings are less frequent than medium ratings.
* The dataset can be used to identify pricing and stock trends.

## Business Value

This type of scraping workflow can be used for:

* competitor monitoring
* market research
* price tracking
* product availability analysis
