def add_elements(arr, k):
    """
    Return the sum of elements with at most two digits from the first k elements of arr.
    An element qualifies if its absolute value has at most two digits (i.e., abs(x) <= 99).
    """
    return sum(x for x in arr[:k] if abs(x) <= 99)
