from decimal import Decimal, ROUND_HALF_DOWN

def closest_integer(value: str) -> int:
    s = value.strip()
    if 'e' in s.lower():
        dec = Decimal(str(float(s)))
    else:
        dec = Decimal(s)
    result = dec.quantize(Decimal('1'), rounding=ROUND_HALF_DOWN)
    return int(result)
