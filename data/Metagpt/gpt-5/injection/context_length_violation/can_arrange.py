def can_arrange(arr):
    """
    Return the largest index i such that arr[i] < arr[i-1].
    If no such index exists, return -1.
    """
    last = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            last = i
    return last
