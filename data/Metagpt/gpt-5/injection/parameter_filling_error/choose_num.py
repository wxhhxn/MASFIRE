import math


def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive.
    If there's no such number, then the function should return -1.
    """
    if x > y:
        return -1
    candidate = math.floor(y)
    if candidate % 2 != 0:
        candidate -= 1
    if candidate < x:
        return -1
    return candidate
