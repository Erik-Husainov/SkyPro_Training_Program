import pytest
from src.masks import *


def test_get_mask_card_number():
    assert get_mask_card_number('1234567890123456') == '1234 56** **** 3456'
    assert get_mask_card_number('12345678') == 'Недействительный номер карты'
    assert get_mask_card_number('') == 'Недействительный номер карты'


def test_get_mask_account():
    assert get_mask_account('123456789') == '**6789'
    assert get_mask_account('') == 'Недействительный номер счета'