import json
from requests import Session
from bs4 import BeautifulSoup


class Client(object):

    def __init__(self):
        self.base_url = 'https://polisen.se'
        self.api_route = self.base_url + '/api/listingservice'
        self.location_route = self.api_route + '/locationsuggestions'
        self.items_route = self.api_route + '/items'
        self.session = Session()

    def get_suggestions(self, location):
        try:
            return json.loads(
                self.session.get(
                    self.location_route + '?query=' + location,
                ).text
            )
        except ValueError:
            return []

    def get_items(self, location_id):
        try:
            return map(
                lambda x: self.set_attr(x, 'text', self.scrape_element_text(
                    self.base_url + x['Url'], '.editorial-html'
                )),
                json.loads(
                    self.session.post(
                        self.items_route,
                        data={
                            'SelectedLocationId': location_id,
                            'ContentId': 7069,
                            'PageIndex': 1,
                            'IncludeChildIndexes': False,
                            'FilterOnSelectedLocation': True,
                            'filter': None,
                            'GeoAreaType': 1,
                            'Latitude': 0,
                            'Longitude': 0,
                            'ListItemType': 1,
                            'PropertyIds': []
                        }
                    ).text
                )['List']
            )
        except ValueError:
            return []

    def set_attr(self, item, attr, value):
        item[attr] = value
        return item

    def scrape_element_text(self, url, selector):
        return BeautifulSoup(self.session.get(url).text, 'html.parser')\
            .select(selector)[0].text
