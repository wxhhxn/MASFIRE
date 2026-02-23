def compare_one(a, b):
    """
    Takes integers, floats, or strings representing real numbers (supports '.' or ',' as decimal separator).
    Returns the larger original variable (preserving its original type/representation). Returns None if numerically equal.
    """
    def to_number(x):
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            s = x.strip().replace(',', '.')
            return float(s)
        raise TypeError('Unsupported type')

    va = to_number(a)
    vb = to_number(b)
    if va == vb:
        return None
    return a if va > vb else b
