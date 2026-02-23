from math import sqrt

def triangle_area(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return -1
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq <= 0:
        return -1
    area = sqrt(area_sq)
    return round(area, 2)
