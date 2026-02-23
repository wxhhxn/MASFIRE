def factorize(n):
    """Return the list of prime factors of n in non-decreasing order.

    Examples:
    >>> factorize(12)
    [2, 2, 3]
    >>> factorize(13)
    [13]
    >>> factorize(1)
    []
    """
    if n <= 1:
        return []
    factors = []
    # extract factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    import math
    limit = math.isqrt(n) + 1
    while p <= limit and n > 1:
        while n % p == 0:
            factors.append(p)
            n //= p
            limit = math.isqrt(n) + 1
        p += 2
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print([])
        else:
            print(factorize(num))
