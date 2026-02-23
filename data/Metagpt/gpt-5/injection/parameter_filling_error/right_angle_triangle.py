from math import isclose


def right_angle_triangle(a, b, c):
    x, y, z = sorted((float(a), float(b), float(c)))
    if x <= 0.0 or y <= 0.0 or z <= 0.0:
        return False
    if x + y <= z:
        return False
    return isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-9)
