from decimal import Decimal
from typing import Any


def compare_one(a: Any, b: Any):
    def to_decimal(x: Any) -> Decimal:
        if isinstance(x, str):
            s = x.strip().replace(',', '.')
            return Decimal(s)
        if isinstance(x, float):
            return Decimal(str(x))
        if isinstance(x, int):
            return Decimal(x)
        raise TypeError('Unsupported type')

    va = to_decimal(a)
    vb = to_decimal(b)

    if va == vb:
        return None
    return a if va > vb else b
