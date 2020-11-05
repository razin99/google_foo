import pytest
from solution import solution

def test_1():
    assert solution(3, [7, 3, 5, 1]) == [-1,7,6,3]


def test_2():
    assert solution(5, [19, 14, 28]) == [21,15,29]
