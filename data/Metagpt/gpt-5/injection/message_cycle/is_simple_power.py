def is_simple_power(x: int, n: int) -> bool:
    """Return True if there exists a non-negative integer k such that n**k == x; otherwise False.
    Edge cases:
    - if n == 1 -> return x == 1
    - if n == 0 -> return x in {0, 1}
    - if n == -1 -> return x in {-1, 1}
    For other n:
    - if x == 1 -> True
    - if x <= 0 -> False
    - else iteratively divide x by n while x % n == 0 and check if x reduces to 1.
    """
    if n == 1:
        return x == 1
    if n == 0:
        return x in (0, 1)
    if n == -1:
        return x in (-1, 1)

    if x == 1:
        return True
    if x <= 0:
        return False

    while x % n == 0:
        x //= n
    return x == 1
