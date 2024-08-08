from datetime import datetime

from src.widget import get_date


def filter_by_state(dicts_list: list, state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и опциональный параметр state и возвращает новый список словарей,
    у которых соответствующий state"""

    return [i for i in dicts_list if i['state'] == state]


def sort_by_date(dicts_list: list, sort_way: bool = True) -> list:
    return [sorted(dicts_list, key=lambda x: datetime.strptime(get_date(x['date']), "%d.%m.%Y"),
                   reverse=(not sort_way))]
