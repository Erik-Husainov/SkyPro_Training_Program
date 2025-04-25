import re
from collections import Counter


def seek_substring(dicts_list: list[dict], substring: str) -> list:
    """Функция ищет подстроку в списке словарей и возврщает список словарей в которых обнаружена подстрока"""

    regex = re.compile(substring, re.IGNORECASE)
    return [
        item for item in dicts_list
        if any(regex.search(str(value)) for value in item.values())
    ]


def counting_transactions_in_categories(dicts_list: list[dict], categories: list) -> dict:
    """Функция подсчитывает количество транзакций в категориях"""

    count = []

    for item in dicts_list:
        if item['description'] in categories:
            count.append(item['description'])
    ans = Counter(count)
    return ans
