def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Logic: The minimum sum of four positive even numbers is 2+2+2+2 = 8. Any even n >= 8 works.
    return n % 2 == 0 and n >= 8
