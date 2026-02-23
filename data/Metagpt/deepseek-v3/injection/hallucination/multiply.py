import os
import math

def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits (last two digits).
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Get last two digits of each number
    unit_a = abs(a) % 100
    unit_b = abs(b) % 100
    
    # Multiply the unit digits
    return unit_a * unit_b