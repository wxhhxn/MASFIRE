def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Numbers starting with 1: 1 followed by any (n-1) digits = 10^(n-1)
    # Numbers ending with 1: any (n-1) digits followed by 1 = 10^(n-1)
    # Numbers both starting and ending with 1: 1 followed by any (n-2) digits followed by 1 = 10^(n-2)
    # Using inclusion-exclusion principle:
    return 2 * (10 ** (n - 1)) - (10 ** (n - 2)) if n > 1 else 1