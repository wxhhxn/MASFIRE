def smallest_change(arr):
    """
    Given an array arr of integers, return the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array reads the same
    forwards and backwards. One change can change any single element to any other value.

    Examples:
    smallest_change([1,2,3,5,4,7,9,6]) == 8
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 2
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    changes = 0
    for i in range(n):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
    return changes
