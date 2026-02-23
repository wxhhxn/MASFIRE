def is_equal_to_sum_even(n: int) -> bool:
    \"\"
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    \"\"
    # The sum of four positive even integers is even and at least 2+2+2+2 = 8.
    return (n % 2 == 0) and (n >= 8)
