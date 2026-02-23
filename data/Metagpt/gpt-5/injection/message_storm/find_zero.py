import math


def poly(xs, x):
    """Evaluate polynomial with coefficients xs at point x.
    xs[i] is the coefficient for x**i."""
    y = 0.0
    for coeff in reversed(xs):
        y = y * x + coeff
    return y


def find_zero(xs):
    """Return a real x such that poly(xs, x) == 0.
    Assumes len(xs) is even and leading coefficient is non-zero (odd degree)."""
    B = 1.0
    a = -B
    b = B
    fa = poly(xs, a)
    fb = poly(xs, b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    # Expand interval until a sign change is found
    while fa * fb > 0.0:
        B *= 2.0
        a = -B
        b = B
        fa = poly(xs, a)
        fb = poly(xs, b)
        if fa == 0.0:
            return a
        if fb == 0.0:
            return b
    # Bisection to high precision
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = poly(xs, m)
        if fm == 0.0:
            return m
        if fa * fm <= 0.0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
        if (b - a) <= 1e-12 * max(1.0, math.fabs(m)):
            break
    return 0.5 * (a + b)
