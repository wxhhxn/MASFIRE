from math import isclose, isfinite


def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    """
    # Basic validation: numeric (excluding booleans), finite, positive
    for s in (a, b, c):
        if isinstance(s, bool) or not isinstance(s, (int, float)):
            return False
        if not isfinite(s) or s <= 0:
            return False

    # Sort sides so that z is the largest; check triangle inequality
    x, y, z = sorted((float(a), float(b), float(c)))
    if x + y <= z:
        return False

    # Pythagorean check with tolerance to handle floating point inputs
    return isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-9)
