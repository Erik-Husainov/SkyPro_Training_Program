import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('C:/Users/Пользователь/PycharmProjects/pythonPoetry/logs/utils.log', mode='w')
file_formatter = logging.Formatter('masks %(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_num: str) -> str:
    """Функция, возвращающая маску номера по правилу ХХХХ ХХ** **** ХХХХ"""

    logger.info('Start get_mask_card_number')
    if len(card_num) == 16:
        card_num = str(card_num)
        logger.info('End function')
        return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[12:]}"
    logger.error('invalid number')
    return 'Недействительный номер карты'


def get_mask_account(acc_num: str) -> str:
    """Функция, возвращающая маску номера по правилу **ХХХХ"""
    logger.info('start get_mask_account')
    if len(acc_num) > 5:
        acc_num = str(acc_num)
        logger.info('success')
        return f"**{acc_num[-4:]}"
    logger.error('invalid number')
    return 'Недействительный номер счета'

