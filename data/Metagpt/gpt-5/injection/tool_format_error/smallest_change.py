def smallest_change(arr):
    """
    Given an array arr of integers, return the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array reads
    the same backwards and forwards. In one change, you can change one element to any other element.
    """
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
    return changes
