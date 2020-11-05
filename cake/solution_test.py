from solution import solution

def test_1():
    assert solution("abcabcabcabc") == 4


def test_2():
    assert solution("abccbaabccba") == 2

def test_3():
    assert solution("beefcakebeefcakebeefcakebeefcakebeefcake") == 5

