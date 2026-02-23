import math

def choose_num(x: float, y: float) -> int:
    """
    Returns the biggest even integer within [x, y] inclusive.
    Returns -1 if no such number exists.
    x and y are positive numbers (int or float).
    """
    if x > y:
        return -1
    top = math.floor(y)
    if top % 2 != 0:
        top -= 1
    lower = math.ceil(x)
    if top >= lower:
        return top
    return -1
