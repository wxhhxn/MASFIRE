from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def closest_integer(value):
    s = value.strip()
    try:
        num = Decimal(s)
    except (InvalidOperation, AttributeError):
        raise ValueError("Invalid number string")
    return int(num.quantize(Decimal(1), rounding=ROUND_HALF_UP))
