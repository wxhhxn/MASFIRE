def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    result = []
    for x in l:
        # Exclude booleans (since bool is a subclass of int) and keep only ints/floats > 0
        if isinstance(x, bool):
            continue
        if isinstance(x, (int, float)) and x > 0:
            result.append(x)
    return result
