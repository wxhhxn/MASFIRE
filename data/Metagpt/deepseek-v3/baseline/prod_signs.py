def prod_signs(arr):
    """
    Calculate the sum of magnitudes multiplied by the product of all signs in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        int or None: Result of calculation or None for empty array
    
    Examples:
        >>> prod_signs([1, 2, 2, -4]) == -9
        True
        >>> prod_signs([0, 1]) == 0
        True
        >>> prod_signs([]) is None
        True
    """
    if not arr:
        return None
    
    magnitude_sum = 0
    sign_product = 1
    
    for num in arr:
        magnitude_sum += abs(num)
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        else:
            sign_product = 0
    
    return magnitude_sum * sign_product