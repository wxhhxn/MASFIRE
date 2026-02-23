def sum_squares(lst: list[int]) -> int:
    """
    Compute the sum of list entries after transforming by index rules.

    For each index i:
    - If i is a multiple of 3: square lst[i].
    - Else if i is a multiple of 4 (and not a multiple of 3): cube lst[i].
    - Otherwise leave lst[i] unchanged.

    Examples:
    >>> sum_squares([1, 2, 3])
    6
    >>> sum_squares([])
    0
    >>> sum_squares([-1, -5, 2, -1, -5])
    -126
    """
    total = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            y = x * x
        elif i % 4 == 0:
            y = x * x * x
        else:
            y = x
        total += y
    return total
