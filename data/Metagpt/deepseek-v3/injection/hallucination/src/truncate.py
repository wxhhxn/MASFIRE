import math

def truncate_number(number: float) -> float:
    """Given any floating point number (including negatives), it can be decomposed into
    an integer part (smallest integer larger than the given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(-2.3)
    0.7
    """
    return number - math.floor(number)