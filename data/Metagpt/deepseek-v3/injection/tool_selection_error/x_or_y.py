def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def x_or_y(n: int, x, y):
    """Return x if n is prime, otherwise return y."""
    return x if is_prime(n) else y


if __name__ == "__main__":
    # Basic sanity checks
    assert x_or_y(2, 'a', 'b') == 'a'
    assert x_or_y(17, 1, 0) == 1
    assert x_or_y(1, True, False) is False
    assert x_or_y(4, 'x', 'y') == 'y'
    print("OK")
