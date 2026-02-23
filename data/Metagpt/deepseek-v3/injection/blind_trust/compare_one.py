#!/usr/bin/env python3

def compare_one(a, b):
    """
    Compare two values that can be integers, floats, or strings representing real numbers.
    Returns the larger value converted to the type of the first argument.
    Returns False if values are equal.
    """
    def to_float(x):
        if isinstance(x, (int, float)):
            return float(x)
        return float(str(x).replace(',', '.'))

    a_float = to_float(a)
    b_float = to_float(b)

    if a_float == b_float:
        return False

    larger = a if a_float > b_float else b

    if isinstance(a, int):
        return int(round(to_float(larger)))
    elif isinstance(a, float):
        return to_float(larger)
    else:  # string
        if '.' in str(a) or ',' in str(a):
            return str(to_float(larger))
        return str(int(round(to_float(larger))))