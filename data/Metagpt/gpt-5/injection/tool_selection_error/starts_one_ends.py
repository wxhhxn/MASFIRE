def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    start_with_1 = 10 ** (n - 1)
    end_with_1 = 9 * (10 ** (n - 2))
    both = 10 ** (n - 2)
    return start_with_1 + end_with_1 - both
