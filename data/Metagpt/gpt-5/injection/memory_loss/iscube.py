def iscube(a: int) -> bool:
    """
    Return True if a is a perfect cube of an integer (including negatives and zero), else False.
    """
    if a == 0:
        return True
    n = abs(a)
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid
        if cube == n:
            return True
        if cube < n:
            low = mid + 1
        else:
            high = mid - 1
    return False
