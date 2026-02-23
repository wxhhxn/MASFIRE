import math

def is_happy(s: str) -> bool:
    """Check if a string is happy according to the given criteria.
    A string is happy if:
    1. The sum of its Unicode code points is divisible by 7
    2. The last character is a vowel (a, e, i, o, u, case-insensitive)
    """
    if not s:
        return False
    
    # Check last character is vowel
    last_char = s[-1].lower()
    if last_char not in {'a', 'e', 'i', 'o', 'u'}:
        return False
    
    # Calculate sum of Unicode code points
    total = sum(ord(char) for char in s)
    
    # Check if divisible by 7
    return total % 7 == 0