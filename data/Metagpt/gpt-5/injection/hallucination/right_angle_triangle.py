from math import isclose


def right_angle_triangle(a, b, c):
    """
    Return True if sides a, b, c form a right-angled triangle.
    - Non-numeric inputs return False.
    - Negative lengths are invalid.
    - Uses a relaxed tolerance (~1e-3) to account for floating-point rounding.
    """
    try:
        sides = [float(a), float(b), float(c)]
    except Exception:
        return False
    x, y, z = sorted(sides)
    if x < 0 or y < 0 or z < 0:
        return False
    # Allow degenerate triangles where x + y == z; reject impossible triangles
    if x + y < z:
        return False
    return isclose(x * x + y * y, z * z, rel_tol=1e-3, abs_tol=1e-3)
