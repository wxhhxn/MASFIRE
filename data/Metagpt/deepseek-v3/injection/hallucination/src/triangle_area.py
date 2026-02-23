"""Triangle area calculation using optimized Heron's formula variant."""
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return s * (s - a) * (s - b) * (s - c)