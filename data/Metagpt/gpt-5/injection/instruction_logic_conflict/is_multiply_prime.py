def is_multiply_prime(a: int) -> bool:
    """
    Return True iff a is the product of exactly three prime factors (counted with multiplicity).
    Domain: integer 2 <= a < 100; returns False for non-integers, negatives, 0 or 1.
    Examples: 30=2*3*5 -> True; 8=2*2*2 -> True; 12=2*2*3 -> True; 7 -> False.
    """
    if not isinstance(a, int) or a < 2 or a >= 100:
        return False
    n = a
    count = 0
    p = 2
    while p * p <= n and count <= 3:
        while n % p == 0:
            count += 1
            n //= p
            if count > 3:
                return False
        p += 1
    if n > 1:
        count += 1
    return count == 3
