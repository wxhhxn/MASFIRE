from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have equal length")
    
    result = []
    for char_a, char_b in zip(a, b):
        if char_a not in ('0', '1') or char_b not in ('0', '1'):
            raise ValueError("Input strings must contain only '0' or '1'")
        result.append('1' if char_a != char_b else '0')
    return ''.join(result)