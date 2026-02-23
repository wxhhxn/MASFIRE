def sum_squares(lst):
    """
    Take a list of integers. For each index i:
    - If i is a multiple of 3, square the integer.
    - If i is a multiple of 4 and not a multiple of 3, cube the integer.
    - Otherwise leave the integer unchanged.
    Return the sum of all resulting entries.

    Examples:
    - [1, 2, 3] -> 6
    - [] -> 0
    - [-1, -5, 2, -1, -5] -> -126
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val * val
        elif i % 4 == 0 and i % 3 != 0:
            total += val ** 3
        else:
            total += val
    return total
