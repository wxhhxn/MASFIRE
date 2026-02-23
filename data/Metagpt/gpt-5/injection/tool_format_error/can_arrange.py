def can_arrange(arr):
    """
    Returns the largest index i such that arr[i] < arr[i - 1].
    If no such index exists, returns -1.
    Assumes the list has no duplicate values.
    """
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1
