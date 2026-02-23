def maximum(arr, k):
    """
    Given an array arr of integers and a non-negative integer k, return a sorted list
    of length k with the maximum k numbers in arr.

    Examples:
        arr = [-3, -4, 5], k = 3 -> [-4, -3, 5]
        arr = [4, -4, 4], k = 2 -> [4, 4]
        arr = [-3, 2, 1, 2, -1, -2, 1], k = 1 -> [2]

    Notes:
        - 0 <= k <= len(arr)
        - The result must be sorted in ascending order.
        - Duplicates are preserved.
    """
    if k == 0:
        return []
    return sorted(arr)[-k:]
