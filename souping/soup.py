import re
import logging

from bs4 import BeautifulSoup


from locators.main_item import MainItemLocator
from pages.page import Pages

logger = logging.getLogger('scraping.soup')


class Soup:
    def __init__(self, page):
        logger.debug('parsing page with beautiful soup for Single list')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def souping(self):
        logger.debug(f'Finding all book in page using {MainItemLocator.MAIN}')
        locator = MainItemLocator.MAIN
        soup_result_tags = self.soup.select(locator)
        return [Pages(e) for e in soup_result_tags]

    @property
    def paging(self):
        logger.debug(f'Finding all pages with the lists {Soup.paging}')
        locator = MainItemLocator.PAGES
        soup_pager = self.soup.select_one(locator).string

        logger.info(f'Data Found {soup_pager}')

        pattern = 'Page [0-9]+ of ([0-9]+)'
        match = re.search(pattern, soup_pager)
        logger.debug(f"Extracted number: '{match}")
        return int(match.group(1))



