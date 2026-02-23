from string import ascii_lowercase
from typing import Dict

# Precompute lookup table for lowercase letters a-z mapped to 1-26
_LOWERCASE_VALUES: Dict[str, int] = {chr(i): i - 96 for i in range(97, 123)}

def digitSum(s: str) -> int:
    """Calculate the sum of lowercase characters' 1-based ASCII values in a string.
    
    Args:
        s: Input string to process
    
    Returns:
        Sum of 1-based ASCII values for lowercase letters (a=1, z=26).
        Non-lowercase characters are ignored (value=0).
    """
    return sum(_LOWERCASE_VALUES.get(c, 0) for c in s)

# Simple unit test
assert digitSum('abc') == 1 + 2 + 3
assert digitSum('') == 0
assert digitSum('ABC') == 0
assert digitSum('aAaaaXa') == 1 + 1 + 1 + 1 + 0 + 1
assert digitSum('helloE') == 8 + 5 + 12 + 12 + 15 + 0