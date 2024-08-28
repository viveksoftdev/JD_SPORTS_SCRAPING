
# Requirements
### Python 3.7 or higher
### requests
### beautifulsoup4
### aiohttp
### pandas (if needed for data handling)
### re (standard library, no installation required)

# Code Structure
### fetch_pages/
### fetch_page.py: Contains fetch_page and main functions for asynchronous data fetching.
### parser/
### main_parser.py: Contains MainParser class to parse product information from HTML.
### extract_and_parse.py: Contains ExractAndParse class to manage fetching and parsing.
### fetch_pages/
### link_extractor.py: Contains link_extract function to extract product links using CSS selectors.
### Locators/
### all_locators.py: Contains MAIN_LOCATORS class with CSS selectors and regex patterns.

# Code Overview
### fetch_page.py: Contains asynchronous functions to fetch page content.
### link_extractor.py: Extracts product links from a main page.
### main_parser.py: Parses product details from HTML content.
### extract_and_parse.py: Manages fetching and parsing of product data.
### all_locators.py: Contains CSS selectors and regex patterns used for scraping.
