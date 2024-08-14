import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_num, expected_result', [('1234567890123456', '1234 56** **** 3456'),
                                                       ('12345678', 'Недействительный номер карты'),
                                                       ('', 'Недействительный номер карты')])
def test_get_mask_card_number(card_num: str, expected_result: str) -> None:
    assert get_mask_card_number(card_num) == expected_result


@pytest.mark.parametrize('acc_num, expected_result', [('123456789', '**6789'), ('', 'Недействительный номер счета')])
def test_get_mask_account(acc_num: str, expected_result: str) -> None:
    assert get_mask_account(acc_num) == expected_result
