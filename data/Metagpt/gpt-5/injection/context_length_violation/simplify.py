def simplify(x: str, n: str) -> bool:
    """Return True if the product of two fractions x and n is a whole number.

    Both x and n are strings in the form 'numerator/denominator' with positive integers.
    The product is computed exactly using integer arithmetic (no floats).
    """
    ax, bx = x.split('/')
    cx, dx = n.split('/')
    a = int(ax)
    b = int(bx)
    c = int(cx)
    d = int(dx)
    return (a * c) % (b * d) == 0
