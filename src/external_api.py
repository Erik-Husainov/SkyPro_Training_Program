import os
from utils import json_to_dicts_list
import requests
from dotenv import load_dotenv

load_dotenv()


def return_transaction_amount(transaction) -> float:
    """Функция принимает JSON-файл с транзакцией и возвращает сумму транзакции в рублях"""

    json_to_dict = json_to_dicts_list(transaction)
    currency_code = json_to_dict['operationAmount']['currency']['code']
    transaction_sum = float(json_to_dict['operationAmount']['amount'])

    if currency_code == 'RUB':
        return transaction_sum

    else:
        url = (f'https://api.apilayer.com/exchangerates_data/convert?to=RUB'
               f'&from={currency_code}&amount={transaction_sum}')
        headers = {'apikey': os.getenv('EXCHANGE_APIKEY')}
        response = requests.get(url, headers=headers).json()
        return response['result']
