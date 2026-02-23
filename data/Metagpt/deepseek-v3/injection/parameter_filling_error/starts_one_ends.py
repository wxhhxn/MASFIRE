def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    
    # Total numbers starting with 1: 1 * 10^(n-1)
    start_with_1 = 10 ** (n - 1)
    
    # Total numbers ending with 1: 9 * 10^(n-2) * 1 (for n >= 2)
    end_with_1 = 9 * (10 ** (n - 2)) if n >= 2 else 1
    
    # Numbers that both start and end with 1 (to avoid double counting)
    both = 10 ** (n - 2) if n >= 2 else 1
    
    return start_with_1 + end_with_1 - both