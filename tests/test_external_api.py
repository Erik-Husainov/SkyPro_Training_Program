from unittest.mock import patch
from src.external_api import return_transaction_amount


@patch('requests.get')
def test_return_transaction_amount(mock_get, json_example_correct, json_example_euro):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                              'info': {'timestamp': 1744734364, 'rate': 82.552197},
                              'date': '2025-04-15', 'result': 678692.15585}

    assert return_transaction_amount(json_example_correct) == 678692.15585

    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'EUR', 'to': 'RUB', 'amount': 31957.58},
                                               'info': {'timestamp': 1744817044, 'rate': 94.352628},
                                               'date': '2025-04-16', 'result': 3015281.65752}

    assert return_transaction_amount(json_example_euro) == 3015281.65752
