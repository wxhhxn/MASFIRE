def pluck(arr):
    """
    Find and return the smallest even value in the list along with its index.

    Parameters:
        arr: A list of non-negative integers.

    Returns:
        A list [value, index] where value is the smallest even integer in arr and index is
        its position. If arr is empty or contains no even values, return [].
        If multiple occurrences of the smallest even value exist, the one with the
        smallest index is chosen.
    """
    min_val = None
    min_idx = -1

    for i, v in enumerate(arr):
        if v % 2 == 0:
            if (min_val is None) or (v < min_val) or (v == min_val and i < min_idx):
                min_val = v
                min_idx = i

    return [] if min_val is None else [min_val, min_idx]
