def is_equal_to_sum_even(n: int) -> bool:
    """Return True if n can be written as the sum of exactly four positive even numbers."""
    return (n % 2 == 0) and (n >= 8)
