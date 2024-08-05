from widget import get_date


def filter_by_state(dicts_list: list, state: str = 'EXECUTED'):
    """Функция принимает список словарей и опциональный параметр state и возвращает новый список словарей,
    у которых соответствующий state"""

    return [i for i in dicts_list if i['state'] == state]


def sort_by_date(dicts_list: list, sort_way: bool = True):
    return [sorted(dicts_list, key=lambda x: get_date(x['date']), reverse=(not(sort_way)))]



