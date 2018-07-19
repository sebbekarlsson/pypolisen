import json
from requests import Session
from bs4 import BeautifulSoup
from pypolisen.utils import try_except, set_attr
from pypolisen.constants import (
    ITEM_PAGE_TEXT_CSS_QUERY,
    GET_ITEMS_QUERY_DEFAULTS,
    ITEM_META_IGNORE,
    EMPTY_LIST
)


class Client(object):

    def __init__(self):
        self.base_url = 'https://polisen.se'
        self.api_route = self.base_url + '/api/listingservice'
        self.location_route = self.api_route + '/locationsuggestions'
        self.items_route = self.api_route + '/items'
        self.session = Session()

    def _get_suggestions(self, args):
        return json.loads(
            self.session.get(
                self.location_route + '?query=' + args.location,
            ).text
        )

    def get_suggestions(self, location):
        return try_except(
            self._get_suggestions,
            ValueError,
            lambda x: EMPTY_LIST,
            args=dict(location=location)
        )

    def _get_items(self, args):
        return map(
            lambda x: set_attr(x, 'meta', self.get_item_extras(x)),
            json.loads(
                self.session.post(
                    self.items_route,
                    data=dict(
                        SelectedLocationId=args.location_id,
                        **GET_ITEMS_QUERY_DEFAULTS
                    )
                ).text
            )['List']
        )

    def get_items(self, location_id):
        return try_except(
            self._get_items,
            (ValueError, KeyError),
            lambda x: EMPTY_LIST,
            args=dict(location_id=location_id)
        )

    def get_item_document(self, item):
        return BeautifulSoup(
            self.session.get(self.base_url + item['Url']).text,
            'html.parser'
        )

    def get_document_extras(self, document):
        return dict(
            text=try_except(
                lambda x: document.select(ITEM_PAGE_TEXT_CSS_QUERY)[0].text,
                IndexError,
                lambda x: None
            ),
            **{
                meta.get('name'): meta.get('content')
                for meta in document.select('meta')
                if meta.get('name') not in ITEM_META_IGNORE
            }
        )

    def get_item_extras(self, item):
        return self.get_document_extras(self.get_item_document(item))

    def scrape_element_text(self, document, selector):
        return try_except(
            lambda x: document.select(selector)[0].text,
            IndexError,
            lambda x: None
        )
