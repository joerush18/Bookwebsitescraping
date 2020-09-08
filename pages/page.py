import re
import logging

from locators.items import ItemLocator


logger = logging.getLogger('scraping.pages')


class Pages:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'parent is {parent}')
        self.parent = parent

    def __repr__(self):
        return f'Name: {self.title} Price: Rs.{self.price} Rating: {self.rating} Stars'

    @property
    def title(self):
        logger.debug('Finding Title')
        locator = ItemLocator.TITLE
        title = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Title Found {title}')
        return title

    @property
    def price(self):
        logger.debug('Finding Price')
        locator = ItemLocator.PRICE
        price = self.parent.select_one(locator).string
        pattern = '£([0-9]+.[0-9]+)'

        float_price = (re.search(pattern, price))
        logger.debug(f'Title Found {float_price}')
        return float(float_price.group(1))

    @property
    def rating(self):
        locator = ItemLocator.RATING
        rating = self.parent.select_one(locator)
        rating_class = rating.attrs['class']
        rating_final = [star for star in rating_class if star != 'star-rating']
        return Pages.RATINGS[(rating_final[0])]

