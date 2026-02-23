def can_arrange(arr):
    """Return the largest index i such that arr[i] < arr[i-1].

    If no such index exists (including empty or single-element arrays), return -1.
    Assumes the array contains no duplicate values.
    """
    n = len(arr)
    if n < 2:
        return -1
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1
