def smallest_change(arr):
    """
    Return the minimum number of element changes needed to make arr palindromic.
    One change can set any single element to any value.

    Args:
        arr (list[int]): The input list of integers.

    Returns:
        int: Minimum number of changes required to make the list palindromic.
    """
    n = len(arr)
    count = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            count += 1
    return count
