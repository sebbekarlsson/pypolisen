from pypolisen.Client import Client

client = Client()


def test_get_items():
    items = client.get_events()

    assert isinstance(items, list)
    assert len(items) > 0


def test_items():
    items = client.get_events()

    for item in items:
        assert 'id' in item
        assert 'datetime' in item
        assert 'name' in item
        assert 'summary' in item
        assert 'url' in item
        assert 'type' in item
        assert 'location_name' in item
        assert 'location_gps' in item
