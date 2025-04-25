import convertations
import generators
import processing
import searches
import utils
import widget


def main(file_path):
    """Принимает путь к файлу и выводит информацию о транзакциях в соответствии с ответами пользователя"""

    print("""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями.""")
    file_choice = 0
    while str(file_choice) not in ['1', '2', '3']:
        file_choice = input("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")

    file_choice_answer = {'1': 'JSON', '2': 'CSV', '3': 'XLSX'}
    print(f'Для обработки выбран {file_choice_answer[file_choice]}-файл.')

    if file_choice == '1':
        file = utils.json_to_dicts_list(file_path)
    elif file_choice == '2':
        file = convertations.csv_to_dict(file_path)
    elif file_choice == '3':
        file = convertations.xlsx_to_dict(file_path)

    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status_choice = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
        if status_choice.upper() in valid_statuses:
            break
        print(f'Статус операции {status_choice} недоступен.')
    file = searches.seek_substring(file, status_choice)
    print(f'Операции отфильтрованы по статусу {status_choice.upper()}')
    print(file)
    while True:
        filter_by_date = input('Отсортировать операции по дате? Да/Нет')
        if filter_by_date.capitalize() in ['Да', 'Нет']:
            while True:
                dict_filt = {'по возрастанию': True, 'по убыванию': False}

                filter_ascend_descend = input('Отсортировать по возрастанию/убыванию?').lower()
                if filter_ascend_descend in dict_filt:
                    break
                print('Принимаются только "по возрастанию"/"по убыванию"')

            file = processing.sort_by_date(file, dict_filt[filter_ascend_descend])
            break
        print('Принимаются ответы только "Да" или "Нет"')
    print(file)
    while True:
        filter_rub = input('Выводить только рублевые транзакции? Да/Нет')
        if filter_rub.capitalize() in ['Да', 'Нет']:
            if filter_rub.capitalize() == 'Да':
                file = list(generators.filter_by_currency(file, 'RUB'))
            break
        print('Принимаются ответы только "Да" или "Нет"')
    print(file)

    while True:
        filter_spec_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        if filter_spec_word.capitalize() in ['Да', 'Нет']:
            if filter_spec_word.capitalize() == 'Да':
                spec_word = input('Введите слово для фильтрации: ')
                file = searches.seek_substring(file, spec_word)
            break
    print(file)
    print('Распечатываю итоговый список транзакций...')
    if len(file) > 0:
        print(f'Всего банковских операций в выборке: {len(file)}\n')

        for i in file:
            print(f'{widget.get_date(i['date'])} {i['description']}')
            if 'from' in i:
                if i['from'] != '':
                    print(f'{widget.mask_account_card(i['from'])} -> {widget.mask_account_card(i['to'])}')
            else:
                print(f'{widget.mask_account_card(i['to'])}')
            if file_choice == '1':
                print(f'Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n')
            else:
                print(f'Сумма: {i['amount']} {i['currency_name']}\n')

    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
