def get_mask_card_number(card_num: str) -> str:
    '''Функция, возвращающая маску номера по правилу ХХХХ ХХ** **** ХХХХ'''
    if len(card_num) == 16:
        card_num = str(card_num)
        return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[12:]}"
    return 'Недействительный номер карты'


def get_mask_account(acc_num: str) -> str:
    '''Функция, возвращающая маску номера по правилу **ХХХХ'''
    if len(acc_num) > 5:
        acc_num = str(acc_num)
        return f"**{acc_num[-4:]}"
    return 'Недействительный номер счета'
