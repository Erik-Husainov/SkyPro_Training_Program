import masks


def mask_account_card(acc_card: str) -> str:
    if len(acc_card.split()[-1]) == 20:
        return f'{' '.join(acc_card.split()[:-1])} {masks.get_mask_account(int(acc_card.split()[-1]))}'

    return f'{' '.join(acc_card.split()[:-1])} {masks.get_mask_card_number(int(acc_card.split()[-1]))}'


def get_date(date: str) -> str:
    return '.'.join(date[:10].split('-')[::-1])
