
import csv
from logger import initialize_logger
import logging
from scraper import scrape_page



def main():
    initialize_logger()
    logging.info("Web scraper started.")

    # Open the CSV file for writing and set up the CSV writer
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])
        logging.info("CSV file created successfully. Starting to scrape quotes...")
        
        for i in range(1, 6):
            quotes = scrape_page(i)
            for quote, author in quotes:
                writer.writerow([quote, author])
                logging.info(f"Quote from page {i} has been successfully saved to quotes.csv")
        logging.info("Web scraper finished successfully. All quotes have been saved to quotes.csv")


if __name__ == "__main__":
    main()        
            