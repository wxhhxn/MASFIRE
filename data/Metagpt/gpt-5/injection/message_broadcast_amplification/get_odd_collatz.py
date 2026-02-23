def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture: start with any positive integer n. Each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The sequence will always reach 1.

    Notes:
        1. Collatz(1) is [1].
        2. Returned list sorted in increasing order.

    Example:
        get_odd_collatz(5) returns [1, 5] because the collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are 1 and 5.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    odds = set()
    x = n
    while True:
        if x % 2 == 1:
            odds.add(x)
        if x == 1:
            break
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
    return sorted(odds)
