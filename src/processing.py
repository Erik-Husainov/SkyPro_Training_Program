from widget import get_date


def filter_by_state(dicts_list: list, state: str = 'EXECUTED'):
    """Функция принимает список словарей и опциональный параметр state и возвращает новый список словарей,
    у которых соответствующий state"""

    return [i for i in dicts_list if i['state'] == state]


