def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    
    # Total n-digit numbers: 9 * 10^(n-1) (first digit 1-9, others 0-9)
    # Numbers starting with 1: 1 * 10^(n-1) (first digit fixed to 1, others 0-9)
    # Numbers ending with 1: 9 * 10^(n-2) * 1 (first digit 1-9 except 1, middle digits 0-9, last digit fixed to 1)
    # But we've double-counted numbers that both start and end with 1: 1 * 10^(n-2) * 1 (first digit 1, middle digits 0-9, last digit 1)
    
    total_start_with_1 = 10 ** (n - 1)
    total_end_with_1 = 9 * 10 ** (n - 2)
    both_start_and_end_with_1 = 10 ** (n - 2)
    
    return total_start_with_1 + total_end_with_1 - both_start_and_end_with_1