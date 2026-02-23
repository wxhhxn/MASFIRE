def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers.
    Examples:
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == True
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0 and n >= 6
