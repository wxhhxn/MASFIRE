def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only the number 1
    
    # Count numbers starting with 1: 1 * 10^(n-1)
    start_with_1 = 10 ** (n - 1)
    
    # Count numbers ending with 1: 9 * 10^(n-2) for n >= 2
    end_with_1 = 9 * 10 ** (n - 2)
    
    # Subtract the overlap (numbers that both start and end with 1)
    overlap = 10 ** (n - 2) if n >= 2 else 0
    
    return start_with_1 + end_with_1 - overlap