import math
from decimal import Decimal

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number expressed as percentage.
    >>> truncate_number(3.5)
    50.0
    """
    integer_part = int(number)
    fractional_part = number - integer_part
    return fractional_part * 100.0