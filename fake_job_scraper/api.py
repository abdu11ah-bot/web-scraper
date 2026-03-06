import requests
from util import BASE_URL, TIMEOUT, HEADER 
import logging

def fetch_jobs():
    try:
        response = requests.get(BASE_URL, headers=HEADER, timeout=TIMEOUT)
        response.raise_for_status()
        logging.info("Successfully fetched job listings")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")
        return None
    
