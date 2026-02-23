def get_odd_collatz(n):
    """
    Return a sorted ascending list of unique odd integers encountered in the Collatz sequence starting from n, including 1.
    The Collatz sequence is defined as:
      - if n is even: n = n // 2
      - if n is odd:  n = 3*n + 1
    The sequence ends when n reaches 1.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    odd_set = set()
    while True:
        if n % 2 == 1:
            odd_set.add(n)
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return sorted(odd_set)
