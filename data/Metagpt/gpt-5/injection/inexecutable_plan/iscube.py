def iscube(a):
    if a == 0:
        return True
    x = -a if a < 0 else a
    low, high = 0, x if x > 1 else 1
    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid
        if cube == x:
            return True
        if cube < x:
            low = mid + 1
        else:
            high = mid - 1
    return False
