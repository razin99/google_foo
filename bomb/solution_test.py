import pytest
from solution import solution

def test_1():
    assert solution('4', '7') == '4'


def test_2():
    assert solution('2', '1') == '1'


def test_3():
    assert solution('2', '4') == 'impossible'


def test_4():
    assert solution('4', '3') == '3'


def test_4():
    a = '1' + '0' * 3
    b = long(a) - 1
    assert solution('1', a) == str(b)
