import json
from requests import Session
from bs4 import BeautifulSoup
from pypolisen.utils import tryreturn, set_attr
from pypolisen.constants import (
    ITEM_PAGE_TEXT_CSS_QUERY,
    GET_ITEMS_QUERY_DEFAULTS,
    EMPTY_LIST
)


class Client(object):

    def __init__(self):
        self.base_url = 'https://polisen.se'
        self.api_route = self.base_url + '/api/listingservice'
        self.location_route = self.api_route + '/locationsuggestions'
        self.items_route = self.api_route + '/items'
        self.session = Session()

    def get_suggestions(self, location):
        return tryreturn(
            json.loads(
                self.session.get(
                    self.location_route + '?query=' + location,
                ).text
            ),
            ValueError,
            EMPTY_LIST
        )

    def get_items(self, location_id):
        return tryreturn(
            map(
                lambda x: set_attr(x, 'text', self.get_item_text(x)),
                json.loads(
                    self.session.post(
                        self.items_route,
                        data=dict(
                            SelectedLocationId=location_id,
                            **GET_ITEMS_QUERY_DEFAULTS
                        )
                    ).text
                )['List']
            ),
            ValueError,
            EMPTY_LIST
        )
    
    def get_item_document(self, item):
        return BeautifulSoup(
            self.session.get(self.base_url + item['Url']).text,
            'html.parser'
        )

    def get_item_text(self, item):
        return self.scrape_element_text(
            self.get_item_document(item),
            ITEM_PAGE_TEXT_CSS_QUERY
        )

    def scrape_element_text(self, document, selector):
        return tryreturn(
            document.select(selector)[0].text,
            IndexError,
            None
        )
