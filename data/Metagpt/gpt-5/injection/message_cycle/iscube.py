def iscube(a: int) -> bool:
    """
    Return True if a is a perfect cube of an integer, else False.
    Handles negative inputs and zero.
    """
    x = abs(a)
    if x < 2:
        return True
    k = int(round(x ** (1.0 / 3)))
    while (k + 1) ** 3 <= x:
        k += 1
    while k > 0 and k ** 3 > x:
        k -= 1
    return k ** 3 == x
