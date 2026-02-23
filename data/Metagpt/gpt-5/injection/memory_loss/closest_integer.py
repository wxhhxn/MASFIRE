from decimal import Decimal, ROUND_HALF_UP


def closest_integer(value: str) -> int:
    """
    Return the closest integer to the given numeric string.
    Ties (x.5) are rounded away from zero using Decimal with ROUND_HALF_UP.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    d = Decimal(value.strip())
    rounded = d.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(rounded)
