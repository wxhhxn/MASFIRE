def count_up_to(n):
    """Return a list of prime numbers strictly less than n.

    Examples:
    - count_up_to(5) -> [2, 3]
    - count_up_to(11) -> [2, 3, 5, 7]
    - count_up_to(0) -> []
    - count_up_to(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
    - count_up_to(1) -> []
    - count_up_to(18) -> [2, 3, 5, 7, 11, 13, 17]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 2:
        return []

    sieve = bytearray(b"\x01") * n
    sieve[0:2] = b"\x00\x00"  # 0 and 1 are not prime

    limit = int(n ** 0.5) + 1
    for p in range(2, limit):
        if sieve[p]:
            start = p * p
            sieve[start:n:p] = b"\x00" * (((n - 1 - start) // p) + 1)

    return [i for i in range(2, n) if sieve[i]]
