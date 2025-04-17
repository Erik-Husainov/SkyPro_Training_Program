import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('utils %(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter((file_formatter))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def json_to_dicts_list(json_file) -> list[dict]:
    """Функция принимает JSON-файл и возвращает в виде списка словарей
    Если JSON нерабочий, возвращается пустой список"""

    logger.info('Start json_to_dict_list')
    try:
        if '{' not in json_file:
            logger.info('open file')
            with open(json_file, encoding='utf-8') as f:
                dicts_list = json.load(f)

        else:
            logger.info('reading JSON-string')
            dicts_list = json.loads(json_file)
        logger.info('Convertation success')
        return dicts_list
    except  Exception:
        logger.error('JSON is unreadable')
        return []

print(json_to_dicts_list('data/operations.json'))

