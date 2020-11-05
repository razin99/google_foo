import pytest
from solution import solution

def test_1():
    assert solution(1,1) == "1"


def test_2():
    assert solution(3,2) == "9"


def test_3():
    assert solution(5,10) == "96"
