def can_arrange(arr):
    """Return the largest index i such that arr[i] < arr[i - 1].
    If no such index exists, return -1.
    The input array contains no duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) -> 3
    can_arrange([1,2,3]) -> -1
    """
    if not arr or len(arr) < 2:
        return -1
    last_break = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            last_break = i
    return last_break
