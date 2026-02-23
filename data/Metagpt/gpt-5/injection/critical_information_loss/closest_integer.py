from decimal import Decimal, ROUND_HALF_UP


def closest_integer(value: str) -> int:
    """
    Return the closest integer to the numeric-string input 'value'.
    Ties (.5) are rounded away from zero.
    """
    d = Decimal(value)
    return int(d.to_integral_value(rounding=ROUND_HALF_UP))
