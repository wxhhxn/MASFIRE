def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.
    """
    if not arr:
        return None
    sign_prod = 1
    for x in arr:
        if x == 0:
            return 0
        sign_prod *= 1 if x > 0 else -1
    total = sum(abs(x) for x in arr)
    return sign_prod * total
