def pluck(arr):
    """
    Given an array of non-negative integers, return [smallest_even_value, its index],
    where the smallest_even_value is the smallest even number in arr. If multiple
    occurrences exist, choose the one with the smallest index. If there are no
    even values or arr is empty, return [].
    """
    min_val = None
    min_idx = -1
    for idx, val in enumerate(arr):
        if val % 2 == 0:
            if min_val is None or val < min_val:
                min_val = val
                min_idx = idx
    return [] if min_val is None else [min_val, min_idx]
