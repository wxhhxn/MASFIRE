import numpy as np

def string_sequence(n: int) -> str:
    """ Return a string containing comma-delimited numbers starting from 1 up to n inclusive.
    >>> string_sequence(0)
    '1'
    >>> string_sequence(5)
    '1, 2, 3, 4, 5'
    """
    if n < 1:
        return '1'
    return ', '.join(str(i) for i in range(1, n+1))