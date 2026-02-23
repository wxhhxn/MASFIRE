def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    
    Args:
        n: int - the number to check
        
    Returns:
        bool: True if n can be expressed as sum of 4 positive even numbers, False otherwise
        
    Examples:
        >>> is_equal_to_sum_even(4)
        False
        >>> is_equal_to_sum_even(6)
        False
        >>> is_equal_to_sum_even(8)
        True
    """
    # The smallest sum of 4 positive even numbers is 2+2+2+2=8
    # For n >= 8 and even, it can be expressed as sum of 4 positive even numbers
    # For n=6, the minimal possible sum is 2+2+2+2=8 which is >6
    return n >= 8 and n % 2 == 0