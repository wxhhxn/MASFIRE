import math

def intersection(interval1, interval2):
    left = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    if left > right:
        return 'NO'
    length = right - left
    if length < 2:
        return 'NO'
    if length == 2:
        return 'YES'
    if length % 2 == 0:
        return 'NO'
    limit = math.isqrt(length)
    i = 3
    while i <= limit:
        if length % i == 0:
            return 'NO'
        i += 2
    return 'YES'
