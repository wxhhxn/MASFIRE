import math

def closest_integer(value: float) -> int:
    x = float(value)
    return int(math.copysign(math.floor(abs(x) + 0.5), x))
