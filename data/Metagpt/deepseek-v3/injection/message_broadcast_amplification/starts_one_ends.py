def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    
    # Total n-digit numbers: from 10^(n-1) to 10^n - 1
    total_n_digit = 9 * (10 ** (n - 1))
    
    # Numbers starting with 1: 1 followed by (n-1) digits
    start_with_one = 10 ** (n - 1)
    
    # Numbers ending with 1: first digit 1-9, middle digits 0-9, last digit 1
    end_with_one = 9 * (10 ** (n - 2)) if n > 1 else 1
    
    # Numbers that both start and end with 1 (to avoid double counting)
    both_start_end_one = 10 ** (n - 2) if n > 1 else 1
    
    # Using inclusion-exclusion principle
    return start_with_one + end_with_one - both_start_end_one