def pluck(arr):
    """
    Return [smallest_even_value, its_index] for the given list of non-negative integers.
    If no even values or arr is empty, return [].
    """
    if not arr:
        return []

    min_value = None
    min_index = -1

    for idx, val in enumerate(arr):
        if val % 2 == 0:
            if min_value is None or val < min_value:
                min_value = val
                min_index = idx

    return [] if min_value is None else [min_value, min_index]
