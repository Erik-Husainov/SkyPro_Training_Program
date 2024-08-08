from src import masks


def mask_account_card(acc_card: str) -> str:
    """Функция возвращает маску счета или карты в соответвующем формате"""

    if len(acc_card.split()[-1]) == 20:
        return f'{' '.join(acc_card.split()[:-1])} {masks.get_mask_account(acc_card.split()[-1])}'

    return f'{' '.join(acc_card.split()[:-1])} {masks.get_mask_card_number(acc_card.split()[-1])}'


def get_date(date: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""

    return '.'.join(date[:10].split('-')[::-1])
