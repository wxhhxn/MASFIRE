import json5
from digit_utils import extract_digits
from validators import validate_numbers
from config import ODD_DIGIT_MASK

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    validate_numbers(nums)
    
    for num in nums:
        if num > 10:
            digits = extract_digits(abs(num))
            if digits:
                first = digits[0]
                last = digits[-1]
                if (first % 2 == 1) and (last % 2 == 1):
                    count += 1
    return count