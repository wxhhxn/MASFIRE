import math

def right_angle_triangle(a, b, c):
    """
    Return True if sides a, b, c can form a right-angled triangle, False otherwise.
    Validates positivity and triangle inequality, supports int/float inputs.
    """
    try:
        x, y, z = sorted(float(s) for s in (a, b, c))
    except (TypeError, ValueError):
        return False

    # All sides must be positive
    if x <= 0 or y <= 0 or z <= 0:
        return False

    # Triangle inequality
    if x + y <= z:
        return False

    # Right angle check with tolerance for floating point
    return math.isclose(z * z, x * x + y * y, rel_tol=1e-9, abs_tol=1e-12)
