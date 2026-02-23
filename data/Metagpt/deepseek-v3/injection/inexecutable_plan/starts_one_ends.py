def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
    Args:
        n (int): The number of digits
        
    Returns:
        int: Count of n-digit numbers starting or ending with 1
    """
    # Numbers starting with 1: 1 followed by any (n-1) digits
    # Numbers ending with 1: any first (n-1) digits followed by 1
    # To avoid double-counting numbers that both start and end with 1,
    # we use inclusion-exclusion principle
    
    # Total numbers starting with 1: 1 * 10^(n-1)
    starts_with_1 = 10 ** (n - 1)
    
    # Total numbers ending with 1: 9 * 10^(n-2) * 1 (first digit can't be 0)
    if n == 1:
        ends_with_1 = 1
    else:
        ends_with_1 = 9 * (10 ** (n - 2))
    
    # Numbers that both start and end with 1: 1 * 10^(n-2) * 1
    if n == 1:
        both = 1
    else:
        both = 10 ** (n - 2)
    
    return starts_with_1 + ends_with_1 - both