import logging
import requests
from util import BASE_URL, TIMEOUT, HEADER
from logger import setup_logger
from save_into_csv import save_jobs_to_csv

def main():
    setup_logger()
    logging.info("Starting job scraper")
    
    try:
        response = requests.get(BASE_URL, headers=HEADER, timeout=TIMEOUT)
        response.raise_for_status()
        logging.info("Successfully fetched job listings")
        save_jobs_to_csv()
    except requests.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")

