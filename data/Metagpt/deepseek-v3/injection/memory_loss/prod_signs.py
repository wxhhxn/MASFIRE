def prod_signs(arr):
    """
    Calculates the sum of magnitudes multiplied by the product of signs for an array of integers.
    Returns None for empty array.
    
    Args:
        arr: List of integers
        
    Returns:
        int or None: Result of calculation or None for empty array
        
    Examples:
        >>> prod_signs([1, 2, 2, -4]) == -9
        >>> prod_signs([0, 1]) == 0
        >>> prod_signs([]) == None
    """
    if not arr:
        return None
    
    product = 1
    sum_magnitudes = 0
    
    for num in arr:
        if num > 0:
            product *= 1
            sum_magnitudes += num
        elif num < 0:
            product *= -1
            sum_magnitudes += -num
        else:  # num == 0
            product *= 0
            sum_magnitudes += 0
    
    return product * sum_magnitudes