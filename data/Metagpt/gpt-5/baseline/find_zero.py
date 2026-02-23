import math



def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x**2 + ... + xs[n] * x**n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))



def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(xs, x) = 0.
    Returns only one zero point, even if there are many.
    Only accepts xs having an even number of coefficients and a non-zero leading coefficient, which guarantees a real solution.
    """
    n = len(xs)
    if n == 0 or n % 2 != 0 or xs[-1] == 0:
        raise ValueError("xs must have an even number of coefficients and a non-zero leading coefficient")
    # Bracket a root; odd-degree polynomial guarantees sign change across large bounds
    a, b = -1.0, 1.0
    fa = poly(xs, a)
    fb = poly(xs, b)
    k = 0
    while fa * fb > 0:
        k += 1
        a = -2.0 ** k
        b = 2.0 ** k
        fa = poly(xs, a)
        fb = poly(xs, b)
        if k > 60:
            break
    tol = 1e-12
    max_iter = 200
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = poly(xs, m)
        if abs(fm) <= tol:
            return m
        if fa * fm <= 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    return 0.5 * (a + b)