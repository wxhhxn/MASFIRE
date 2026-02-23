def iscube(a: int) -> bool:
    b = abs(a)
    lo, hi = 0, max(1, b)
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == b:
            return True
        if cube < b:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
