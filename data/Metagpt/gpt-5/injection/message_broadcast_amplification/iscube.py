def iscube(a):
    n = abs(a)
    lo, hi = 0, max(1, n)
    while lo <= hi:
        mid = (lo + hi) // 2
        m3 = mid * mid * mid
        if m3 == n:
            return True
        elif m3 < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
