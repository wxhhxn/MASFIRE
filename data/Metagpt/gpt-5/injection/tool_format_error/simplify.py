def simplify(x, n):
    """Return True if x * n is a whole number, where x and n are fraction strings 'numerator/denominator'."""
    ax, bx = map(int, x.split("/"))
    an, bn = map(int, n.split("/"))
    return (ax * an) % (bx * bn) == 0
