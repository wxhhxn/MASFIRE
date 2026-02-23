def add_elements(arr, k):
    """
    Return the sum of elements with at most two digits (ignoring sign)
    from the first k elements of arr.

    Example:
        add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) -> 24
    """
    return sum(x for x in arr[:k] if abs(x) <= 99)
