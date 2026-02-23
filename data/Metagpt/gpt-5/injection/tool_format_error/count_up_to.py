from math import isqrt


def count_up_to(n):
    """Return a list of all prime numbers strictly less than n."""
    if n <= 2:
        return []
    primes = []
    for k in range(2, n):
        if k == 2:
            primes.append(2)
            continue
        if k % 2 == 0:
            continue
        limit = isqrt(k)
        i = 3
        is_p = True
        while i <= limit:
            if k % i == 0:
                is_p = False
                break
            i += 2
        if is_p:
            primes.append(k)
    return primes
