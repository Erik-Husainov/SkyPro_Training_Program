import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('state,  expected', [('EXECUTED', [{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'},
                                                            {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}]),
                                              ('CANCELED', [{'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
                                                            {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'}])])
def test_filter_by_state(coll: list, state: str, expected: list) -> None:
    assert filter_by_state(coll, state) == expected


def test_sort_by_date(coll: list) -> None:
    assert sort_by_date(coll) == [[{'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'},
                                   {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
                                   {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'},
                                   {'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'}]]
    assert sort_by_date(coll, False) == [[{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'},
                                          {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'},
                                          {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
                                          {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'}]]
