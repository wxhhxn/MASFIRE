def right_angle_triangle(a, b, c):
    a, b, c = sorted([int(a), int(b), int(c)])
    return a*a + b*b == c*c