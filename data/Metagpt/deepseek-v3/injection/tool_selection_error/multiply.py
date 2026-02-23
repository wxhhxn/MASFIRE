def multiply(a: int, b: int) -> int:
    """Return the product of the unit (ones) digits of a and b.

    Examples:
    >>> multiply(12, 34)
    8
    >>> multiply(-7, 5)
    35
    """
    return (abs(a) % 10) * (abs(b) % 10)
