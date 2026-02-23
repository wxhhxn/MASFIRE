import math

def iscube(a):
    if isinstance(a, bool):
        a = int(a)
    if isinstance(a, int):
        A = a
    elif isinstance(a, float):
        if not math.isfinite(a) or not a.is_integer():
            return False
        A = int(a)
    else:
        try:
            A = int(a)
            if float(A) != float(a):
                return False
        except Exception:
            return False
    n = abs(A)
    if n == 0:
        return True
    low, high = 0, 1
    while high ** 3 < n:
        high *= 2
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == n:
            return True
        if cube < n:
            low = mid + 1
        else:
            high = mid - 1
    return False
