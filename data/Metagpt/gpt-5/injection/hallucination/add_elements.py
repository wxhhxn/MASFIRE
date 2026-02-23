def add_elements(arr, k):
    """
    Return the sum of elements in arr[:k] whose absolute value has exactly two digits.

    An element x qualifies if 10 <= abs(x) <= 99.

    Args:
        arr (list): List of integers (each in the range [-999, 999]).
        k (int): Number of leading elements to consider (0 <= k <= len(arr)).

    Returns:
        int: Sum of qualifying elements from the first k elements of arr.
    """
    total = 0
    for x in arr[:k]:
        ax = abs(x)
        if 10 <= ax <= 99:
            total += x
    return total
