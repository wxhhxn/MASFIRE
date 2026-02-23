def sort_even(l: list) -> list:
    """
    Return a new list where values at odd indices remain the same as in l,
    and values at even indices are replaced by the even-indexed values of l
    sorted in ascending order.

    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    n = len(l)
    # Extract and sort values from even indices
    even_values = sorted(l[0:n:2])
    # Build the result by placing sorted even values back at even positions
    result = list(l)
    j = 0
    for i in range(0, n, 2):
        result[i] = even_values[j]
        j += 1
    return result
