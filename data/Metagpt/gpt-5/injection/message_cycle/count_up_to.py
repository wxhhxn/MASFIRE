def count_up_to(n):
    """Return a list of prime numbers less than n."""
    if n is None or n <= 2:
        return []
    sieve = [True] * n
    sieve[0:2] = [False, False]
    limit = int(n ** 0.5) + 1
    for p in range(2, limit):
        if sieve[p]:
            start = p * p
            sieve[start:n:p] = [False] * len(range(start, n, p))
    return [i for i in range(2, n) if sieve[i]]
