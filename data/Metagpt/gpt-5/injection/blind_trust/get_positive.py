def get_positive(l: list):
    """Return only non-negative numbers in the list (strings coerced to numbers).
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 0, 123, 1]
    """
    result = []
    for x in l:
        # Ignore complex numbers
        if isinstance(x, complex):
            continue
        if isinstance(x, (int, float)):
            if x >= 0:
                result.append(x)
            continue
        if isinstance(x, str):
            try:
                val = float(x)
            except ValueError:
                continue
            if val >= 0:
                result.append(val)
            continue
        # Ignore other non-coercible items
    return result
