import asyncio
from fetch_pages.fetch_page import main
from parser.main_parser import MainParser




class ExractAndParse:
    """
    A class for fetching content from a list of URLs asynchronously and parsing the product information from the fetched HTML content.

    Attributes:
        url_list (list): A list of URLs to fetch and parse.
        parsed_list (list): A list to store parsed product information dictionaries.

    Methods:
        __init__(url_list):
            Initializes the ExractAndParse class with a list of URLs and triggers the content fetching and parsing process.

        fetch_content_and_parse():
            Asynchronously fetches HTML content from the provided URLs, parses the content, and updates the `parsed_list` with parsed product information.
    """

    def __init__(self,url_list):
        '''
        Initializes the ExractAndParse class with a list of URLs.

        Args:
            url_list (list): A list of URLs from which to fetch and parse HTML content.
        '''

        self.url_list = url_list
        self.parsed_list = []
        
        self.fetch_content_and_parse()
    def fetch_content_and_parse(self):
        """
        Fetches HTML content from the provided URLs asynchronously and parses the product information.

        Uses the `main` function from the `fetch_pages.fetch_page` module to asynchronously fetch HTML content from the URLs. Then, it uses the `MainParser` class to parse the fetched HTML content and extracts product information.

        The parsed product information is appended to the `parsed_list` attribute.

        Updates:
            - `parsed_list`: A list of dictionaries containing parsed product information for each URL.

        Returns:
            list: A list of dictionaries with parsed product information for each URL.
        """

        content = asyncio.run(main(self.url_list))

        for data in content:
            print('parsing')
            self.parsed_list.append(MainParser(data).product_info_dict)
        print('content parsed you can access using parse_list attribute')
        return self.parsed_list
        


