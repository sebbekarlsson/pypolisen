import json
import requests


class Client(object):

    base_url = None
    events = None

    def __init__(self):
        self.base_url = 'https://polisen.se/api/events'

    def download_json_file(self,
                           datetime: str = "",
                           eventlocation: list = [],
                           eventtype: list = []):

        url = self.base_url

        if eventlocation:
            _location = ""
            for _l in eventlocation:
                _location += _l + ";"
            eventlocation = _location

        if eventtype:
            _types = ""
            for _t in eventtype:
                _types += _t + ";"
            eventtype = _types

        if datetime:
            url += "?DateTime={}".format(datetime)
            if eventlocation:
                url += "&locationname={}".format(eventlocation)
            if eventtype:
                url += "&type={}".format(eventtype)
        elif eventlocation:
            url += "?locationname={}".format(eventlocation)
            if eventtype:
                url += "&type={}".format(eventtype)
        elif eventtype:
            url += "?type={}".format(eventtype)

        print(url)
        jsonfile = None
        try:
            jsonfile = requests.get(url)
        except requests.exceptions.InvalidSchema:
            return False
        except requests.exceptions.ConnectionError:
            return False

        # If we didn't get any content or we didn't get HTTP
        # code 200 (OK) we must give up
        if (jsonfile is None) or (jsonfile.status_code != 200):
            return False

        # Load the JSON file
        try:
            self.events = json.loads(jsonfile.text)
        except TypeError:
            return False
        except json.decoder.JSONDecodeError:
            return False

    def load_json_file(self, filename: str):
        with open(filename) as jsonfile:
            self.events = json.load(jsonfile)

    def get_events(self,
                   datetime: str = "",
                   eventlocation: list = [],
                   eventtype: list = []) -> list:

        self.download_json_file(datetime=datetime,
                                eventlocation=eventlocation,
                                eventtype=eventtype)

        events = []
        for event in self.events:
            if event['id'] is not None:
                ev = {
                    'id': event['id'],
                    'datetime': event['datetime'],
                    'name': event['name'],
                    'summary': event['summary'],
                    'url': event['url'],
                    'type': event['type'],
                    'location_name': event['location']['name'],
                    'location_gps': event['location']['gps']
                }
                events.append(ev)
        return events
