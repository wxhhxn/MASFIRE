def can_arrange(arr):
    """Return the largest index i (1-based) where arr[i] < arr[i-1].
    If no such index exists, return 0. Assumes arr may contain duplicate values.
    Examples:
    can_arrange([1,2,4,3,5]) == 4
    can_arrange([1,2,3]) == 0
    """
    res = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            res = i + 1
    return res
