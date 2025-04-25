from typing import Generator


def filter_by_currency(transactions: list, currency: str = 'USD') -> Generator[list, None, None]:
    """Функция принимает на вход список транзакций и необязательный аргумент currency и возвращает
    только те транзакции, у которых соответствующий currency"""
    for transaction in transactions:
        if 'operationAmount' in transaction:
            if transaction['operationAmount']['currency']['code'] == currency:
                yield transaction
        else:
            if transaction['currency_code'] == currency:
                yield transaction



def transaction_descriptions(transactions: list) -> Generator[list, None, None]:
    """Функция принимает на вход список транзакций и возвращает описание каждой транзакции"""
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция принимает начальное и конечное числа и возвращает номера карт в этом промежутке"""
    for i in range(start, end + 1):
        card_num = "{:016d}".format(i)
        card_num = ' '.join(card_num[j:j + 4] for j in range(0, len(card_num), 4))
        yield card_num

