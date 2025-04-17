import json


def json_to_dicts_list(json_file) -> list[dict]:
    """Функция принимает JSON-файл и возвращает в виде списка словарей
    Если JSON нерабочий, возвращается пустой список"""

    try:
        if '{' not in json_file:
            with open(json_file, encoding='utf-8') as f:
                dicts_list = json.load(f)
        else:
            dicts_list = json.loads(json_file)
        return dicts_list
    except  Exception:
        return []

