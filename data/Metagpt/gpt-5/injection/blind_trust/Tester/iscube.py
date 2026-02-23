def iscube(a: int) -> bool:
    """
    Return True if integer a is a perfect cube of some integer, else False.
    Handles negatives and zero correctly.
    """
    if a == 0:
        return True
    abs_a = -a if a < 0 else a
    c = int(abs_a ** (1/3))
    return c ** 3 == abs_a or (c + 1) ** 3 == abs_a

assert iscube(1)
