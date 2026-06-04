# Web Scraping Internship Project

## Project Overview
This project scrapes real-world data from Wikipedia using Python. It extracts 5 different datasets including country populations, highest-grossing films, largest cities, Olympic medals, and tallest buildings.

## Technologies Used
- Python 3
- Requests library (fetch web pages)
- BeautifulSoup4 (parse HTML)
- Pandas (export to CSV)
- VS Code

## Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas

SAMPLE OUTPUT
🚀 STARTING MULTI-PAGE WEB SCRAPER
============================================================
📋 Will scrape 5 different Wikipedia pages

[1/5] Processing...
📥 Scraping: highest_grossing_films
✅ Connected successfully!
✅ SCRAPED: 50 rows × 8 columns

[2/5] Processing...
📥 Scraping: most_populated_countries
✅ Connected successfully!
✅ SCRAPED: 238 rows × 6 columns

============================================================
📊 SCRAPING COMPLETED!
✅ Successfully scraped: 5/5 pages