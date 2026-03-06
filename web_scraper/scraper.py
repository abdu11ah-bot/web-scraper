from bs4 import BeautifulSoup
import logging
import requests
import csv
from logger import initialize_logger
from util import BASE_URL, headers, timeout

initialize_logger()
def scrape_page(page_number):
    try:
        response = requests.get(BASE_URL.format(1), headers=headers, timeout=timeout)
        if response.status_code == 200:
            logging.info("Successfully accessed the website.")
        else:
            logging.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while trying to access the website: {e}")
        return
    
    url = BASE_URL.format(page_number)
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Check if the request was successful
        logging.info(f"Successfully accessed page {page_number}.")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_and_authors = soup.find_all('div', class_='quote')     # Find all quote elements on the page
        logging.info(f"Found {len(quotes_and_authors)} quotes on page {page_number}.")
        
        data=[]
        for quote in quotes_and_authors:
            quote_text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            data.append((quote_text, author))
        logging.info(f"Quotes from page {page_number} have been successfully scraped.")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while trying to access page {page_number}: {e}")
        return []
    
    