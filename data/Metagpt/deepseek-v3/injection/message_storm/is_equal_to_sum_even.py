def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The smallest positive even number is 2
    # The smallest sum of 4 positive even numbers is 2+2+2+2 = 8
    if n < 8:
        return False
    
    # Since all numbers are even, their sum must be even
    if n % 2 != 0:
        return False
    
    # Any even number >= 8 can be expressed as the sum of 4 positive even numbers
    # For example: 
    # n = 8: 2+2+2+2
    # n = 10: 2+2+2+4
    # n = 12: 2+2+2+6 or 2+2+4+4, etc.
    # This pattern continues for all even numbers >= 8
    return True