def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    # If any element is zero, product of signs is zero and result is zero.
    if any(x == 0 for x in arr):
        return 0
    total = sum(abs(x) for x in arr)
    neg_count = sum(1 for x in arr if x < 0)
    sign = -1 if neg_count % 2 else 1
    return sign * total
