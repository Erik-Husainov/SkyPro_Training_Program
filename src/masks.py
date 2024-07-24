def get_mask_card_number(card_num: int) -> str:
    '''Функция, возвращающая маску номера по правилу ХХХХ ХХ** **** ХХХХ'''

    card_num = str(card_num)
    return f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[12:]}"


def get_mask_account(acc_num: int) -> str:
    '''Функция, возвращающая маску номера по правилу **ХХХХ'''

    acc_num = str(acc_num)
    return f"**{acc_num[-4:]}"
