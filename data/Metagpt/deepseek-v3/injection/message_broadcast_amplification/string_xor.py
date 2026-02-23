from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    
    result = []
    for char_a, char_b in zip(a, b):
        if char_a == '1' and char_b == '1':
            result.append('0')
        elif char_a == '0' and char_b == '0':
            result.append('0')
        else:
            result.append('1')
    
    return ''.join(result)