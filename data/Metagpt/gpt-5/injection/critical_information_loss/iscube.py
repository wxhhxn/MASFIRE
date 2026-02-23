def iscube(a: int) -> bool:
    """
    Return True if 'a' is a perfect cube of some integer, else False.
    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    """
    if a == 0:
        return True
    x = a if a >= 0 else -a
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        m3 = mid * mid * mid
        if m3 == x:
            return True
        if m3 < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
