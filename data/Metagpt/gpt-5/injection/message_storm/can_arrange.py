def can_arrange(arr):
    """Return the largest index i such that arr[i] < arr[i-1]. If none, return -1.
    The array has no duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    last = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            last = i
    return last
