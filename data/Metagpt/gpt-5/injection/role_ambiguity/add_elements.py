def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Elements with at most two digits are those whose absolute value is <= 99.
    """
    return sum(x for x in arr[:k] if abs(x) <= 99)
