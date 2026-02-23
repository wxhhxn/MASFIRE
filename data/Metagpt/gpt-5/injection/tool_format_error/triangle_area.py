import math

def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2.0
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq <= 0:
        return -1
    return round(math.sqrt(area_sq), 2)
