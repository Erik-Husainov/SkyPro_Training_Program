import pytest
from  src.processing import *
from .fixture import coll


def test_filter_by_state(coll):
    assert filter_by_state(coll, 'EXECUTED') == [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'}, {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}]
    assert filter_by_state(coll) == [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'}, {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}]
    assert filter_by_state(coll, 'CANCELED') == [{'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'}, {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'}]


def test_sort_by_date(coll):
    assert sort_by_date(coll) == [[{'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}, {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'}, {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'}, {'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'}]]
    # assert sort_by_date(coll, True) ==
    #         [{'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'},
    #          {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
    #          {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'},
    #          {'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'}]
    #
    # assert sort_by_date(coll, False) ==
    #         [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'},
    #          {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'},
    #          {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
    #          {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}]