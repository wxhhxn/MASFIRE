import math


def right_angle_triangle(a: float, b: float, c: float) -> bool:
    try:
        sides = [float(a), float(b), float(c)]
    except (TypeError, ValueError):
        return False
    if any(s <= 0 for s in sides):
        return False
    s1, s2, s3 = sorted(sides)
    if s1 + s2 <= s3:
        return False
    return math.isclose(s1 * s1 + s2 * s2, s3 * s3, rel_tol=1e-9, abs_tol=1e-12)
