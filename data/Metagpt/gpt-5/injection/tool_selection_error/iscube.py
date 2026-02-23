def iscube(a):
    """
    Return True if integer a is a perfect cube of some integer, else False.
    Works for negatives and zero without using floating point.
    """
    n = abs(a)
    if n == 0:
        return True
    lo, hi = 1, n
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == n:
            return True
        if cube < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
