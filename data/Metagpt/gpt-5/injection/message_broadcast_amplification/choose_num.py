import math


def choose_num(x, y):
    """
    Returns the biggest even integer number in the inclusive range [x, y].
    If no such number exists or x > y, returns -1.
    Handles both integer and float inputs by using ceiling for lower bound
    and floor for upper bound.
    """
    if x > y:
        return -1
    lower = math.ceil(x)
    upper = math.floor(y)
    candidate = upper if upper % 2 == 0 else upper - 1
    return candidate if candidate >= lower else -1
