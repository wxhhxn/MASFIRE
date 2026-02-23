import math


def choose_num(x, y):
    """Return the biggest even integer in [x, y] inclusive, or -1 if none.

    Parameters:
        x (float | int): Lower bound (positive number)
        y (float | int): Upper bound (positive number)
    """
    if x > y:
        return -1

    # Largest integer <= y
    upper = math.floor(y)
    # Make it even
    if upper % 2 != 0:
        upper -= 1

    return upper if upper >= x else -1
