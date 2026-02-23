def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    Treats numbers with leading zeros as valid (e.g., '001' is 3-digit).
    Uses formula: count = 2*10^(n-1) - 10^(n-2)
    Returns 1 for n <= 0
    """
    if n <= 0:
        return 1
    return 2 * 10 ** (n - 1) - 10 ** (n - 2)