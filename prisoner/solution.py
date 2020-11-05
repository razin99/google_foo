def solution(x, y):
    #base case
    if (x,y) == (1,1):
        return str(1)

    # | 7
    # | 4 8
    # | 2 5 9
    # | 1 3 6 10
    # +----------

    # y start row
    #   Get start value (column 1)
    #   ID = start value (assign)
    ID = 1
    for row in range(1, y):
        ID += row

    # x = step
    # From start row, initial step:
    #   delta = y + 1 (assign)
    # Repeat for (step - 1):
    #   ID += delta
    #   delta++
    # Return: str(ID)
    delta = y + 1
    for _ in range(x - 1):
        ID += delta
        delta += 1

    return str(ID)
