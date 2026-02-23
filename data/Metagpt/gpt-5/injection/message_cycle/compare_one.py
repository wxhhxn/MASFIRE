def compare_one(a, b):
    def to_float(x):
        if isinstance(x, str):
            s = x.strip().replace(',', '.')
            return float(s)
        if isinstance(x, (int, float)):
            return float(x)
        raise TypeError('Inputs must be int, float, or string representing a real number')

    fa = to_float(a)
    fb = to_float(b)
    if fa == fb:
        return None
    return a if fa > fb else b
