def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    count_start = 10 ** (n - 1)
    count_end = 9 * (10 ** (n - 2))
    count_both = 10 ** (n - 2)
    return count_start + count_end - count_both
