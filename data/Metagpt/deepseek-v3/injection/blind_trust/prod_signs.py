def prod_signs(arr):
    """
    Calculate the sum of magnitudes multiplied by the product of signs of each number in the array.
    
    Args:
        arr: List of integers
        
    Returns:
        int: Result of sum of magnitudes multiplied by product of signs.
             Returns 0 for empty array.
             
    Examples:
        >>> prod_signs([1, 2, 2, -4]) == -10
        True
        >>> prod_signs([0, 1]) == 0
        True
        >>> prod_signs([]) == 0
        True
    """
    if not arr:
        return 0
        
    sum_magnitudes = 0
    product_signs = 1
    
    for num in arr:
        sum_magnitudes += abs(num)
        if num > 0:
            product_signs *= 1
        elif num < 0:
            product_signs *= -1
        else:
            product_signs = 0
    
    return sum_magnitudes * product_signs