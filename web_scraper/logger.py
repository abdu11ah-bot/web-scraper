import logging

def initialize_logger():   
    logging.basicConfig(
        filename = 'webscraper.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

