import math


def poly(xs: list, x: float):
    """
    Evaluate the polynomial defined by coefficients xs at point x.
    Coefficients are in increasing order: xs[0] + xs[1]*x + xs[2]*x**2 + ...
    """
    # Horner's method for numerical stability
    acc = 0.0
    for coeff in reversed(xs):
        acc = acc * x + coeff
    return acc


def find_zero(xs: list):
    """
    Find one real zero of the polynomial with coefficients xs (constant term first).
    Intended for inputs where len(xs) is even and the highest non-zero coefficient
    is non-zero (i.e., odd-degree polynomial), which guarantees at least one real root.
    Returns a single root as a float.
    """
    # Trim trailing zeros in case the highest coefficients are zero
    if not xs:
        return math.nan
    i = len(xs) - 1
    while i > 0 and xs[i] == 0:
        i -= 1
    xs = xs[: i + 1]

    # Handle simple cases
    if len(xs) == 1:
        return 0.0 if xs[0] == 0 else math.nan
    if len(xs) == 2:
        b = xs[1]
        a0 = xs[0]
        if b == 0:
            return math.nan
        return -a0 / b

    # Try to bracket a root: start with a symmetric interval and expand
    a, b = -1.0, 1.0
    fa = poly(xs, a)
    fb = poly(xs, b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b

    max_expand = 200
    k = 0
    while fa * fb > 0 and k < max_expand:
        # Expand toward the side with smaller magnitude to encourage a sign change
        if abs(fa) <= abs(fb):
            a *= 2.0
            fa = poly(xs, a)
            if fa == 0.0:
                return a
        else:
            b *= 2.0
            fb = poly(xs, b)
            if fb == 0.0:
                return b
        k += 1

    # If still not bracketed, perform a bidirectional scan from 0
    if fa * fb > 0:
        left = 0.0
        right = 0.0
        fl = poly(xs, left)
        fr = fl
        step = 1.0
        for _ in range(max_expand):
            right += step
            fr = poly(xs, right)
            if fl * fr <= 0:
                a, b, fa, fb = left, right, fl, fr
                break
            left -= step
            fl = poly(xs, left)
            if fl * fr <= 0:
                a, b, fa, fb = left, right, fl, fr
                break
            step *= 2.0

    # If still not bracketed for some reason, fall back to a wide interval
    if fa * fb > 0:
        a, b = min(a, b), max(a, b)
        fa, fb = poly(xs, a), poly(xs, b)

    # Bisection method
    lo, hi = a, b
    flo, fhi = fa, fb
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fm = poly(xs, mid)
        if fm == 0.0 or (hi - lo) < 1e-12:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm

    return 0.5 * (lo + hi)
