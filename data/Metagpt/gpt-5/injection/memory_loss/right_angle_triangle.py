from math import isclose


def right_angle_triangle(a: float, b: float, c: float) -> bool:
    """Return True if sides a, b, c form a right-angled triangle, else False."""
    try:
        x, y, z = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if x <= 0 or y <= 0 or z <= 0:
        return False
    x, y, z = sorted((x, y, z))
    if x + y <= z:
        return False
    return isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-12)
