import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(
    filename='webscraper.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')


# This script scrapes quotes and their authors from the website "https://quotes.toscrape.com/" and 
# saves them into a CSV file named "quotes.csv". It handles pagination to scrape multiple pages of quotes.
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://quotes.toscrape.com/"
# Make an initial request to check if the website is accessible
try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        logging.info("Successfully accessed the website.")

    # Open the CSV file for writing and set up the CSV writer
        with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Author'])
            logging.info("CSV file created successfully. Starting to scrape quotes...")
            # Loop through the first 5 pages of the website to scrape quotes and authors
            
            for i in range(1, 6):
                url = f"https://quotes.toscrape.com/page/{i}/"
                try:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()  # Check if the request was successful
                        
                    soup = BeautifulSoup(response.text, 'html.parser') # Parse the HTML content of the page using BeautifulSoup
                    quotes = soup.find_all('div', class_='quote')      # Find all quote elements on the page
                    authors = soup.find_all('small', class_='author')  # Find all author elements on the page
                    logging.info(f"Successfully retrieved page {i}. Found {len(quotes)} quotes.")
                    
                    # Loop through the quotes and authors simultaneously and write them to the CSV file
                    for quote, author in zip(quotes, authors):          
                        writer.writerow([quote.text.strip(), author.text.strip()])
                            
                    logging.info(f"Quotes from page {i} have been successfully saved to quotes.csv")
           
                except requests.exceptions.RequestException as e:
                    logging.error(f"An error occurred while trying to access page {i}: {e}")
    else:
        logging.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred while trying to access the website: {e}")
