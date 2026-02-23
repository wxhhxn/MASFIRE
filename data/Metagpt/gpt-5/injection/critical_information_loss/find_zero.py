import math


def find_zero(xs: list):
    if not isinstance(xs, list) or len(xs) == 0 or len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("xs must be a non-empty list with an even number of coefficients and a non-zero leading coefficient")

    eval_at = lambda t: sum(coeff * math.pow(t, i) for i, coeff in enumerate(xs))

    f0 = eval_at(0.0)
    if f0 == 0.0:
        return 0.0

    a, b = -1.0, 1.