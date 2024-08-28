


def link_extract(main_url,soup_obj,css_selector):
    """
    Extracts and constructs a list of URLs to scrape from a given HTML page based on a CSS selector.

    Args:
        main_url (str): The base URL of the website. This will be appended to relative URLs found in the HTML.
        soup_obj (BeautifulSoup): A BeautifulSoup object representing the parsed HTML page.
        css_selector (str): A CSS selector string used to find the relevant links within the HTML content.

    Returns:
        list: A list of full URLs constructed from the base URL and the relative URLs found using the CSS selector.
    """

    urls_to_scrape = []
    
    for link in soup_obj.select(css_selector):
        urls_to_scrape.append(main_url+link.get('href'))
    return urls_to_scrape





