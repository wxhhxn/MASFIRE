from math import modf


def truncate_number(number: float) -> float:
    """Given a positive floating point number, return its decimal part.

    The decimal part is the leftover part smaller than 1 after removing the
    largest integer smaller than the given number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("number must be positive")
    frac, _ = modf(number)
    return frac
