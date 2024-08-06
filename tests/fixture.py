import pytest


@pytest.fixture()
def coll():
    return [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'},
            {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'},
            {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
            {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'}]