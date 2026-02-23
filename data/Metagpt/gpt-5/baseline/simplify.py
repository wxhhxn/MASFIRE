from fractions import Fraction

def simplify(x: str, n: str) -> bool:
    """
    Return True if x * n is a whole number; otherwise False.
    x and n are of the form 'numerator/denominator' with positive integers.
    """
    return (Fraction(x) * Fraction(n)).denominator == 1
