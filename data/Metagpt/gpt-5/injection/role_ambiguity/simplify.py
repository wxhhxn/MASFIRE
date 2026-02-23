from math import gcd


def simplify(x: str, n: str) -> bool:
    """Return True if the product of fractions x and n is a whole number, else False.

    x and n are strings in the form 'numerator/denominator' with positive integers.
    Examples:
    simplify("1/5", "5/1") -> True
    simplify("1/6", "2/1") -> False
    simplify("7/10", "10/2") -> False
    """
    a_num, a_den = map(int, x.split('/'))
    b_num, b_den = map(int, n.split('/'))
    num = a_num * b_num
    den = a_den * b_den
    g = gcd(num, den)
    return (den // g) == 1
