import math


def truncate_number(number: float) -> float:
    """Return the decimal part of a positive floating point number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return math.modf(number)[0]
