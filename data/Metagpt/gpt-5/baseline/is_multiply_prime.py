def is_multiply_prime(a):
    if not isinstance(a, int) or a < 2 or a >= 100:
        return False
    count = 0
    n = a
    d = 2
    while d * d <= n and count <= 3:
        while n % d == 0:
            count += 1
            n //= d
            if count > 3:
                return False
        d = 3 if d == 2 else d + 2
    if n > 1:
        count += 1
    return count == 3
