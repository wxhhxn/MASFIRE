from math import isclose

def right_angle_triangle(a, b, c):
    sides = sorted((a, b, c), reverse=True)
    x, y, z = sides
    if x < 0 or y < 0 or z < 0:
        return False
    if x + y >= z:
        return False
    return isclose(x*x + z*z, y*y, rel_tol=1e-12, abs_tol=1e-12)
