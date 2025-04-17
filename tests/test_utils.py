from src.utils import json_to_dicts_list


def test_json_to_dicts_list(json_example_correct) -> None:
    assert json_to_dicts_list(json_example_correct) == {'id': 41428829, 'state': 'EXECUTED',
                                                'date': '2019-07-03T18:35:29.512364',
                                                'operationAmount': {'amount': '8221.37',
                                                                    'currency': {'name': 'USD', 'code': 'USD'}},
                                                'description': 'Перевод организации',
                                                'from': 'MasterCard 7158300734726758',
                                                'to': 'Счет 35383033474447895560'}

    assert json_to_dicts_list('data/operations_incorrect.json') == []
