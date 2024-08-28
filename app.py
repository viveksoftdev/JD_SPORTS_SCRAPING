import requests
from bs4 import BeautifulSoup
from Locators import all_locators
from fetch_pages.fetch_page import main
from fetch_pages.link_extractor import link_extract
from parser.extract_and_parse import ExractAndParse
from utils.make_csv import write_to_csv

# Define the URL of the main page from which product links will be extracted.
url = 'https://www.global.jdsports.com/page/kids-hub/'

# Send a GET request to the main page URL and fetch the page content.
resp = requests.get(url).content

# Parse the fetched HTML content using BeautifulSoup for easier HTML manipulation.
soup = BeautifulSoup(resp, 'html.parser')

# Define the base URL to construct full URLs from the relative URLs found on the main page.
main_url = 'https://www.global.jdsports.com'

# Extract product links from the main page using the defined CSS selector.
# `link_extract` function will prepend the base URL to each relative URL found.
links = link_extract(main_url, soup, all_locators.MAIN_LOCATORS.links_css)

# Print the list of extracted product links to verify that the extraction was successful.
print(links)

# Create an instance of `ExractAndParse` with the extracted product links.
# This will fetch each product page and parse the relevant details from the HTML content.
parsed_data = ExractAndParse(links)

# Print the parsed product information.
# `parsed_list` contains details such as product name, price, images, description, sizes, and category.

file_name = 'product_info.csv'
write_to_csv(file_name,parsed_data.parsed_list)


