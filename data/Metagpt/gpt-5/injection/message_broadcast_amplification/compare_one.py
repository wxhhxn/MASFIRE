def compare_one(a, b):
    """
    Compare two values that can be int, float, or strings representing real numbers
    (strings may use '.' or ',' as decimal separators). Return the original input
    (preserving type and formatting) that is numerically larger, or None if equal.

    Examples:
    - compare_one(1, 2.5) -> 2.5
    - compare_one(1, "2,3") -> "2,3"
    - compare_one("5,1", "6") -> "6"
    - compare_one("1", 1) -> None
    """

    def to_float(x):
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            s = x.strip().replace(',', '.')
            return float(s)
        raise TypeError("Inputs must be int, float, or str representing a real number")

    va = to_float(a)
    vb = to_float(b)

    if va == vb:
        return None
    return a if va > vb else b
