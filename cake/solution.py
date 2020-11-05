def pattern_ok(s, size):
    checking = s[0:size]
    for i in range(0, len(s), size):
        if checking != s[i:i+size]:
            return False
    else:
        return True


def solution(s):
    if len(s) == 0:
        return 0

    chars = list(dict.fromkeys(s))
    char_per_seg = len(s) // len(chars)

    while char_per_seg > 1:
        # if (len(s)/char_per_seg).is_integer() and pattern_ok(s, len(s)//char_per_seg):
        if len(s) % char_per_seg == 0 and pattern_ok(s, len(s)//char_per_seg):
            return char_per_seg

        char_per_seg -= 1
    return char_per_seg
