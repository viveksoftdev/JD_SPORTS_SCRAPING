import re
from bs4 import BeautifulSoup
from Locators.all_locators import MAIN_LOCATORS



class MainParser:
    """
    A class to parse product information from a given HTML page using BeautifulSoup.

    Attributes:
        page (BeautifulSoup): The parsed HTML content of the page.
        product_info_dict (dict): A dictionary to store parsed product information, including name, price, images, description, sizes, and category.

    Methods:
        __init__(page):
            Initializes the parser with a page's HTML content and parses product information.

        product_info_parser():
            Extracts product details from the page's HTML content and updates the `product_info_dict` dictionary.
    """
    def __init__(self,page):


        self.page = BeautifulSoup(page,'html.parser')
        self.product_info_dict = {
                        
                        'Product_Name': None,
                        'Product_Price':None,
                        'Image_Links': [],
                        'Description': [],
                        'SIZES':[],
                        'Category': None,
                    }
        self.product_info_parser()
    


    def product_info_parser(self):
        '''
        Parses product information from the HTML content and updates the `product_info_dict` dictionary.

        Extracts data from script tags and HTML elements to fill the dictionary with:
            - Product name
            - Product price
            - Image links
            - Product description
            - Available sizes
            - Stock status (in stock or not)

        This method uses regex patterns to extract specific information from script tags and BeautifulSoup selectors
        to retrieve data from HTML elements.

        Updates:
            - `product_info_dict['Product_Name']`: Product name extracted from the HTML.
            - `product_info_dict['Product_Price']`: Product price extracted from the HTML.
            - `product_info_dict['Image_Links']`: List of image URLs associated with the product.
            - `product_info_dict['Description']`: List of description texts related to the product.
            - `product_info_dict['SIZES']`: List of available product sizes.
            - `product_info_dict['Instock']`: Boolean indicating whether the product is in stock.

        Returns:
            dict: A dictionary containing the parsed product information.
        '''

        information = self.page.find_all('script')
        print('parsing information')
        in_stock_pattern = '".*":.*/(InStock)"'#pattern for extracting instock info from information 
        stock_pattern = 'name:"(.*)"' #pattern for extracting instock info from information 


        information_product_stock = information[4] #script tag contains product stock info
        information_product_description = information[5] #script tag contains product description info

        

        for item in information_product_description:
            instock = False
            for item_specs in re.findall(MAIN_LOCATORS.in_stock_pattern,item):
                if item_specs:
                    instock = True
            self.product_info_dict['Instock'] = instock
                
        
        for item in information_product_stock:
            for name in re.findall(MAIN_LOCATORS.stock_pattern,item):
                self.product_info_dict['SIZES'].append(name)



        for item in self.page.select('div#productPage'):
    
            self.product_info_dict['Description'].extend([data.text.strip('\n\t') for data in list(item.select_one(MAIN_LOCATORS.product_description).children)])
            self.product_info_dict['Product_Name'] = item.select_one(MAIN_LOCATORS.name_selector).text
            self.product_info_dict['Product_Price'] = item.select_one(MAIN_LOCATORS.price_selector).text


            for image in item.select(MAIN_LOCATORS.image_container):
                for element  in image.find_all('img'):
                    self.product_info_dict['Image_Links'].append(element.get('src'))
        print('done')
        return self.product_info_dict
