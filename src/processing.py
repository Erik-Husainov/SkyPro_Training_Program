from src.widget import *
from datetime import datetime

def filter_by_state(dicts_list: list, state: str = 'EXECUTED'):
    """Функция принимает список словарей и опциональный параметр state и возвращает новый список словарей,
    у которых соответствующий state"""

    return [i for i in dicts_list if i['state'] == state]


def sort_by_date(dicts_list: list, sort_way: bool = True):
    return [sorted(dicts_list, key=lambda x: datetime.strptime(get_date(x['date']),"%d.%m.%Y"), reverse=(not sort_way))]

print(sort_by_date([{'id': 4, 'state': 'EXECUTED', 'date': '2019-07-03T'},
            {'id': 9, 'state': 'EXECUTED', 'date': '2018-06-30T'},
            {'id': 5, 'state': 'CANCELED', 'date': '2018-09-12T'},
            {'id': 6, 'state': 'CANCELED', 'date': '2018-10-14T'}], 'CANCELED'))