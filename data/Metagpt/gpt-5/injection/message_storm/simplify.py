def simplify(x, n):
    """Return True if x * n evaluates to a whole number, else False.

    Both x and n are string fractions in the form "numerator/denominator" with
    positive whole numbers and non-zero denominators.
    """
    a_str, b_str = x.split('/')
    c_str, d_str = n.split('/')
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    d = int(d_str)
    numerator = a * c
    denominator = b * d
    return numerator % denominator == 0
