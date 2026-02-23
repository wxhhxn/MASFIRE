def pluck(arr):
    """Return [smallest_even_value, 1-based_index_of_choice] or [] if none."""
    if arr is None or len(arr) == 0:
        return []
    min_val = None
    min_idx = 1
    for i, v in enumerate(arr, start=1):
        if v % 2 == 0:
            # pick the latest occurrence when values are equal, using <=
            if min_val is None or v <= min_val:
                min_val = v
                min_idx = i
    return [min_val, min_idx] if min_val is not None else []
