import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize('currency, expected', [('USD', [{"id": 939719570, "state": "EXECUTED",
                                                          "date": "2018-06-30T02:08:58.425572", "operationAmount":
                                                              {"amount": "9824.07", "currency":
                                                                  {"name": "USD", "code": "USD"}},
                                                          "description": "Перевод организации",
                                                          "from": "Счет 75106830613657916952",
                                                          "to": "Счет 11776614605963066702"},
                                                         {"id": 142264268, "state": "EXECUTED",
                                                          "date": "2019-04-04T23:20:05.206878", "operationAmount":
                                                              {"amount": "79114.93", "currency":
                                                                  {"name": "USD", "code": "USD"}},
                                                          "description": "Перевод со счета на счет",
                                                          "from": "Счет 19708645243227258542",
                                                          "to": "Счет 75651667383060284188"}])])
def test_filter_by_currency(transactions: list, currency: str, expected: list) -> None:
    generator = list(filter_by_currency(transactions, currency))
    assert generator[:2] == expected


@pytest.mark.parametrize('expected', ([["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
                                        "Перевод с карты на карту", "Перевод организации"]]))
def test_transaction_descriptions(transactions: list, expected: list) -> None:
    gen_descriptions = transaction_descriptions(transactions)
    lst = []
    for i in range(5):
        lst.append(next(gen_descriptions))
    assert lst == expected


def test_card_number_generator() -> None:
    gen_card_nums = card_number_generator(1, 3)
    assert (next(gen_card_nums)) == '0000 0000 0000 0001'
    assert (next(gen_card_nums)) == '0000 0000 0000 0002'
    assert (next(gen_card_nums)) == '0000 0000 0000 0003'
