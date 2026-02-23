from decimal import Decimal, ROUND_HALF_UP


def closest_integer(value):
    d = Decimal(value.strip())
    return int(d.to_integral_value(rounding=ROUND_HALF_UP))
