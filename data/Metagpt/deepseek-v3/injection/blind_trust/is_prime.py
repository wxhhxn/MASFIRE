def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    False
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    True
    """
    if n <= 1:
        return n == 1
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n // 3:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True