import requests
import logging
from souping.soup import Soup

logging.basicConfig(format='%(asctime)s '
                           '%(levelname)-8s '
                           '[%(filename)s:'
                           '%(lineno)d]'
                           '%(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt' )


logger = logging.getLogger('scraping')
logger.info('Loading books list .............')


page_content = requests.get('http://books.toscrape.com/').content
results = Soup(page_content)
details = results.souping


for page_num in range(1, results.paging):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{page_num+1}.html').content
    logger.debug('Data fetching from all pages.......')
    results = Soup(page_content)
    details.extend(results.souping)





