def prod_signs(arr):
    """
    Returns the product of magnitudes multiplied by the sum of all signs (1, -1, or 0).
    Returns 0 for empty arrays.
    
    Args:
        arr: List of integers
        
    Returns:
        int: Product of magnitudes multiplied by sum of signs
        
    Examples:
        >>> prod_signs([1, 2, 2, -4]) == 32
        >>> prod_signs([0, 1]) == 0
        >>> prod_signs([]) == 0
    """
    if not arr:
        return 0
        
    magnitude_product = 1
    sign_sum = 0
    
    for num in arr:
        magnitude_product *= abs(num)
        if num > 0:
            sign_sum += 1
        elif num < 0:
            sign_sum -= 1
        # 0 doesn't affect sign_sum
    
    return magnitude_product * sign_sum