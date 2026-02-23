import math

def is_simple_power(x, n):
    if n == 1:
        return x == 1
    if x == 1:
        return True
    
    try:
        exponent = round(math.log(x, n))
    except (ValueError, ZeroDivisionError):
        return False
    
    return n ** exponent == x