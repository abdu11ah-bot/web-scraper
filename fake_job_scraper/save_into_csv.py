from bs4 import BeautifulSoup
import csv
from api import fetch_jobs
import logging

def save_jobs_to_csv(filename='fake_jobs.csv'):
    soup = BeautifulSoup(fetch_jobs(), 'html.parser')
    job_elements = soup.find_all('div', class_='card-content')
    logging.info(f"Found {len(job_elements)} job listings to save into CSV")
    
    try:
            
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Company', 'Location', 'Date Posted'])
            logging.info(f"Writing job listings to {filename}")
            
            for job in job_elements:
                title = job.find('h2', class_='title').text.strip()
                company = job.find('h3', class_='company').text.strip()
                location = job.find('p', class_='location').text.strip()
                link = job.find('a')['href']
                writer.writerow([title, company, location, link])
                logging.info(f"Saved job listing: {title}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {e}")