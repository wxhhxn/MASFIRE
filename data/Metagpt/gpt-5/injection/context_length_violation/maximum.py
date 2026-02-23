def maximum(arr, k):
    """
    Return a sorted (ascending) list of length k containing the maximum k numbers from arr.

    Args:
        arr (list[int]): List of integers.
        k (int): Number of maximum elements to return (0 <= k <= len(arr)).

    Returns:
        list[int]: Sorted ascending list of the k largest values from arr.
    """
    if k == 0:
        return []
    arr_sorted = sorted(arr)
    return arr_sorted[-k:]
