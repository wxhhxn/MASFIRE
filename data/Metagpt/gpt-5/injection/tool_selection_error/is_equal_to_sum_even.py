def is_equal_to_sum_even(n: int) -> bool:
    """
    Return True iff the given integer n can be written as the sum of exactly four positive even numbers.

    Examples:
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return (n % 2 == 0) and (n >= 8)
