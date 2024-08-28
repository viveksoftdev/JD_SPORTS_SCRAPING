class MAIN_LOCATORS:

    """
    This class contains CSS selectors and regular expression patterns used for locating and extracting product information
    from a webpage. It is intended for use with web scraping tools to identify and retrieve relevant product details.

    """
    links_css = 'a[data-ip-position^="ProductSpotlight-1__tab--__product-"]'
    name_selector = 'h1[data-e2e="product-name"]'
    price_selector = 'span[data-e2e="product-price"]'
    product_size_container = 'div[id="productSizeStock"]'
    product_description = 'div[class="tab-info"]'
    image_container = 'div[id="gallery"]'

    product_info = 'div#productPage'


    in_stock_pattern = '".*":.*/(InStock)"'#pattern for extracting instock info from information 
    stock_pattern = 'name:"(.*)"' #pattern for extracting instock info from information 