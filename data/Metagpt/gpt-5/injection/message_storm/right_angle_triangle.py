import math

def right_angle_triangle(a, b, c):
    try:
        x, y, z = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return False
    if x <= 0 or y <= 0 or z <= 0:
        return False
    if not (x + y > z and x + z > y and y + z > x):
        return False
    s = sorted([x, y, z])
    return math.isclose(s[0] * s[0] + s[1] * s[1], s[2] * s[2], rel_tol=1e-9, abs_tol=1e-9)
