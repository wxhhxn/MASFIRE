import math


def poly(xs: list, x: float) -> float:
    """Evaluate the polynomial at x using coefficients xs (xs[i] is coefficient for x**i)."""
    result = 0.0
    for coeff in reversed(xs):
        result = result * x + coeff
    return float(result)


def find_zero(xs: list) -> float:
    """Find one real root of the polynomial defined by coefficients xs.

    Preconditions:
    - len(xs) must be even
    - xs[-1] (highest-degree coefficient) must be non-zero

    Method:
    - Bracket the root by symmetric expansion starting from [-1, 1]
    - Apply bisection up to 100 iterations or until interval < 1e-12
    """
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("len(xs) must be even and the highest-degree coefficient xs[-1] must be non-zero.")

    span = 1.0
    a = -span
    b = span

    fa = poly(xs, a)
    if fa == 0.0:
        return a
    fb = poly(xs, b)
    if fb == 0.0:
        return b

    # Expand bracket until a sign change or span limit
    while fa * fb > 0.0 and span <= 1e6:
        span *= 2.0
        a = -span
        b = span
        fa = poly(xs, a)
        if fa == 0.0:
            return a
        fb = poly(xs, b)
        if fb == 0.0:
            return b

    if fa * fb > 0.0:
        raise ValueError("Failed to bracket a root within span limit.")

    # Bisection method
    for _ in range(100):
        mid = (a + b) / 2.0
        fm = poly(xs, mid)
        if fm == 0.0:
            return mid
        if (b - a) < 1e-12:
            break
        if fa * fm < 0.0:
            b = mid
            fb = fm
        else:
            a = mid
            fa = fm

    return (a + b) / 2.0
