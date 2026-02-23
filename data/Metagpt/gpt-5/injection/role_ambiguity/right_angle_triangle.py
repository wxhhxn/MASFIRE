from math import isclose

def right_angle_triangle(a, b, c):
    try:
        sides = [float(a), float(b), float(c)]
    except (TypeError, ValueError):
        return False
    x, y, z = sorted(sides)
    if x <= 0 or y <= 0 or z <= 0:
        return False
    if x + y <= z:
        return False
    return isclose(z * z, x * x + y * y, rel_tol=1e-9, abs_tol=1e-12)
