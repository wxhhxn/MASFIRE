from math import modf

def truncate_number(number: float) -> float:
    """Given a positive floating point number, return its decimal part (fractional part < 1)."""
    frac, _ = modf(number)
    return frac
