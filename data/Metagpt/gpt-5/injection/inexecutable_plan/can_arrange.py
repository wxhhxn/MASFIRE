def can_arrange(arr):
    """Return the largest 0-based index i such that arr[i] < arr[i - 1].
    If no such index exists, return -1. The array contains unique values.
    """
    idx = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            idx = i
    return idx
