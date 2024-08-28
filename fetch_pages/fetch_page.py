import aiohttp
import asyncio


async def fetch_page(url,timeout=10):
    """
    Asynchronously fetches the content of a given URL using aiohttp.

    Args:
        url (str): The URL of the page to fetch.
        timeout (int, optional): The timeout in seconds for the HTTP request. Default is 10 seconds.

    Returns:
        str: The HTML content of the page fetched from the URL.


    """

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(timeout)) as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main(url_list):

    """
    Asynchronously fetches the content of multiple URLs using aiohttp.

    Args:
        url_list (list of str): A list of URLs to fetch.

    Returns:
        list of str: A list containing the HTML content of each page fetched from the URLs.

    Raises:
        asyncio.TimeoutError: If any request times out.
        Exception: For other exceptions that occur during fetching.
    """
    try:
        print(url_list)
        return await asyncio.gather(*(fetch_page(url)for url in url_list))
    except asyncio.TimeoutError as error:
        print(error)
        pass
    except Exception as error:
        print(error)
        pass