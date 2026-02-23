def pluck(arr):
    """
    Find and return the smallest even value in the input iterable together with its index.

    Args:
        arr (iterable): An iterable of integers.

    Returns:
        tuple: (smallest_even_value, index) if an even value exists, otherwise (None, None).

    The function considers only integer values that are even (value % 2 == 0).
    If multiple elements share the same smallest even value, the first occurrence's index is returned.
    """
    smallest = None
    smallest_idx = None

    for idx, val in enumerate(arr):
        # Only consider integers that are even
        if not isinstance(val, int):
            continue
        if val % 2 != 0:
            continue

        if smallest is None or val < smallest:
            smallest = val
            smallest_idx = idx

    if smallest is None:
        return None, None
    return smallest, smallest_idx


if __name__ == "__main__":
    # Basic self-checks
    assert pluck([5, 3, 2, 8, 4]) == (2, 2)
    assert pluck([7, 7, 7]) == (None, None)
    assert pluck([6, 2, 2, 10]) == (2, 1)
    assert pluck([]) == (None, None)
    print("pluck: basic checks passed")
