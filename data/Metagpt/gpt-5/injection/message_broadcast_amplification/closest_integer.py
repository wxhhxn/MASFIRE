from decimal import Decimal, ROUND_HALF_UP


def closest_integer(value: str) -> int:
    d = Decimal(value.strip())
    return int(d.quantize(Decimal(0), rounding=ROUND_HALF_UP))
