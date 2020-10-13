import argparse
import sys
import json
from pypolisen.Client import Client


parser = argparse.ArgumentParser()
parser.add_argument('m')

client = Client()
AVAILABLE_COMMANDS = ['events']


def print_help():
    print('Usage: polisen <method> [--location city] [--type eventtype] [--date YYYY-MM-DD|YYYY-MM|YYYY]')
    print('Available methods: [{}]'.format(', '.join(AVAILABLE_COMMANDS)))


def print_pretty(stdout):
    print(json.dumps(stdout, indent=4, sort_keys=True))


def run_events():
    parser.add_argument(
        '--location',
        metavar='l', type=str, help='location name / city name'
    )
    parser.add_argument(
        '--type',
        metavar='t', type=str, help='event type'
    )
    parser.add_argument(
        '--date',
        metavar='d', type=str, help='date'
    )

    args = parser.parse_args()

    for item in client.get_events(datetime=args.date,
                                  eventlocation=[args.location],
                                  eventtype=[args.type]):
        print_pretty(item)


def run():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command not in AVAILABLE_COMMANDS:
        return print_help()

    if command == 'events':
        run_events()


if __name__ == "__main__":
    run()
