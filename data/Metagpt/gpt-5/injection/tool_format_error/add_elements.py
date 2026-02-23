def add_elements(arr, k):
    """
    Return the sum of elements with at most two digits from the first k elements of arr.
    Elements with at most two digits satisfy abs(x) < 100.
    """
    return sum(x for x in arr[:k] if abs(x) < 100)
