from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def closest_integer(value: str) -> int:
    """
    Takes a string representing a number and returns the closest integer to it.
    If the number is equidistant from two integers, round it away from zero.
    """
    try:
        d = Decimal(value.strip())
    except (InvalidOperation, AttributeError):
        raise ValueError("Invalid numeric string")
    return int(d.quantize(Decimal(1), rounding=ROUND_HALF_UP))
