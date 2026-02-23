import math

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n are string representations of fractions.
    """
    a_str, b_str = x.split('/')
    c_str, d_str = n.split('/')
    a, b = int(a_str), int(b_str)
    c, d = int(c_str), int(d_str)

    g1 = math.gcd(a, d)
    g2 = math.gcd(c, b)

    b //= g2
    d //= g1

    return b * d == 1
