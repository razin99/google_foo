def make_gen(generation, M, F, t_M, t_F):
    if M == t_M and F == t_F:
        return generation

    if M > t_M or F > t_F:
        return None

    a = make_gen(generation + 1, M, M + F, t_M, t_F)
    b = make_gen(generation + 1, M + F, F, t_M, t_F)

    return a if a is not None else b


def solution(x, y):
    target_M = long(x)
    target_F = long(y)
    M = 1
    F = 1
    generation = make_gen(0, M, F, target_M, target_F)
    if generation is None:
        generation = 'impossible'

    return str(generation)
