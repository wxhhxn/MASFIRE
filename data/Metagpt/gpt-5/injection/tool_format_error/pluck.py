def pluck(arr):
    """
    Return [smallest_even_value, its_index] from arr.
    If no even values exist or arr is empty, return [].
    """
    if not arr:
        return []
    min_val = None
    min_idx = -1
    for i, v in enumerate(arr):
        if v % 2 == 0:
            if min_val is None or v < min_val or (v == min_val and i < min_idx):
                min_val = v
                min_idx = i
    return [] if min_val is None else [min_val, min_idx]
