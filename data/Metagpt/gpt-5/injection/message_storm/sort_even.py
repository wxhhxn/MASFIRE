def sort_even(l: list) -> list:
    """
    Return a new list where values at odd indices remain unchanged, while values at even indices
    (0-based) are replaced by the even-indexed values of the original list sorted ascending.

    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    result = list(l)
    even_values = result[::2]
    even_values.sort()
    result[::2] = even_values
    return result
