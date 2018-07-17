# pypolisen
> Python wrapper for `https://polisen.se/aktuellt/polisens-nyheter/`


## Usage
### Fetching location suggestions
> `Client`.`get_suggestions(<str:location_name>)`

    from pypolisen.Client import Client


    client = Client()


    suggestions = client.get_suggestions('Gisla')

    # [
    #     {
    #         'Text': 'Gislaved',
    #         'Value': '69'
    #     }
    #     ...
    # ]

### Fetching items / police notices
> `Client`.`get_items(<int:location_id>)`

    from pypolisen.Client import Client


    client = Client()


    items = client.get_items(69)

    # [
    #     {
    #         'HasImage': False,
    #         'Headline': '06 juli 12.59, Trafikolycka, singel, Gislaved',
    #         'Preamble': '...',
    #         'PublishedDate': '...',
    #         'Url': '...',
    #         'ListItemType': 4,
    #         'ImageUrl': '...',
    #         'ImageDescription': '...',
    #         'HasTeaserText': False,
    #         ...
    #     }
    #     ...
    # ]

### It can also be used through the command line
> Use the command `polisen`:

    # arguments:
    $ polisen <method> <args...>

    # fetching location suggestions
    # arguments: <location_name>
    $ polisen suggestions gisla

    ...

    # fetching items / notices
    # arguments: <location_id>
    $ polisen items 69

## Installing
> To install either clone down the repository and run:

    python setup.py install

> Or using pip:

    pip install pypolisen
