import argparse
import sys
import json
from pypolisen.Client import Client

parser = argparse.ArgumentParser()
parser.add_argument('m')


client = Client()

AVAILABLE_COMMANDS = ['suggestions', 'items']


def print_help():
    print('Usage: polisen <method> <args...>')
    print('Available methods: [{}]'.format(', '.join(AVAILABLE_COMMANDS)))


def run_items():
    parser.add_argument(
        'location_id',
        metavar='i', type=int, help='location id / city id'
    )

    args = parser.parse_args()

    for item in client.get_items(args.location_id):
        print(json.dumps(item, indent=4, sort_keys=True))


def run_suggestions():
    parser.add_argument(
        'location',
        metavar='l', type=str, help='location name / city name'
    )

    args = parser.parse_args()

    for item in client.get_suggestions(args.location):
        print(json.dumps(item, indent=4, sort_keys=True))


def run():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command not in AVAILABLE_COMMANDS:
        return print_help()

    items = []

    if command == 'suggestions':
        run_suggestions()
    elif command == 'items':
        run_items()
