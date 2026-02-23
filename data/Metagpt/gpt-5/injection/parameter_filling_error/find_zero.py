import math


def poly(xs: list, x: float) -> float:
    """Evaluate polynomial sum(coeff * x**i for i, coeff in enumerate(xs))."""
    return sum(coeff * (x ** i) for i, coeff in enumerate(xs))


def find_zero(xs: list) -> float:
    """Return a single real root x such that poly(xs, x) == 0.

    Constraints:
    - Accept only xs with an even number of coefficients and non-zero leading coefficient xs[-1]; otherwise raise ValueError.
    - If len(xs) == 2: linear case, return -xs[0] / xs[1].
    - For higher odd degrees: Use Newton-Raphson from x0 = 0.0 with tol = 1e-12 and max_iter = 200.
      If it fails, fall back to bisection by bracketing and then bisecting to the same tolerance.
    """
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("xs must have even length and a non-zero leading coefficient")

    if len(xs) == 2:
        # Linear case: a0 + a1*x = 0 -> x = -a0/a1
        return -xs[0] / xs[1]

    tol = 1e-12
    max_iter = 200

    # Newton-Raphson starting from x0 = 0.0
    x = 0.0
    for _ in range(max_iter):
        fx = sum(coeff * (x ** i) for i, coeff in enumerate(xs))
        if abs(fx) <= tol:
            return x
        dfx = sum(i * coeff * (x ** (i - 1)) for i, coeff in enumerate(xs) if i > 0)
        if dfx == 0.0:
            break
        x_new = x - fx / dfx
        if abs(x_new - x) <= tol:
            return x_new
        x = x_new

    # Fall back to bisection
    def f(val: float) -> float:
        return sum(coeff * (val ** i) for i, coeff in enumerate(xs))

    low = -1.0
    high = 1.0
    f_low = f(low)
    f_high = f(high)

    bound = 1e6
    while f_low * f_high > 0 and abs(low) <= bound and abs(high) <= bound:
        low *= 2.0
        high *= 2.0
        f_low = f(low)
        f_high = f(high)

    if f_low * f_high > 0:
        # Failed to bracket (should not happen for odd-degree with non-zero leading coefficient)
        raise ValueError("Failed to bracket a root within bounds")

    for _ in range(1000):
        mid = 0.5 * (low + high)
        f_mid = f(mid)
        if abs(f_mid) <= tol or abs(high - low) <= tol:
            return mid
        if f_low * f_mid <= 0:
            high = mid
            f_high = f_mid
        else:
            low = mid
            f_low = f_mid

    return 0.5 * (low + high)
