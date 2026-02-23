def right_angle_triangle(a, b, c):
    sides = sorted([int(a), int(b), int(c)])
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    return sides[0]**2 + sides[1]**2 == sides[2]**2