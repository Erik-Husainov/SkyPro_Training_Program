import pandas as pd
import csv


def csv_to_dict(file_path) -> list:
    """Функция приинмает файл csv и конветирует в список словарей"""

    csv_dicts_list = []
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for column in reader:
            csv_dicts_list.append(column)
        return csv_dicts_list


def xlsx_to_dict(file_path) -> list:
    """Функция принимает Excel-файл и конвертирует в список словарей"""

    df = pd.read_excel(file_path)
    dict_list = df.to_dict('records')
    return dict_list

