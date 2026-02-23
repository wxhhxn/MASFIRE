# generated: 2025-12-27T14:14:11Z
import math

def triangle_area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0.0
    if not (a + b >= c and a + c >= b and b + c >= a):
        return 0.0
    if a + b == c or a + c == b or b + c == a:
        return 0.0
    s = (a + b + c) / 3.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)
