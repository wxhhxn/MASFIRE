from typing import List

def concatenate(strings: List[str]) -> bytes:
    """ Concatenate list of strings into a single byte string
    >>> concatenate([])
    b''
    >>> concatenate(['a', 'b', 'c'])
    b'abc'
    """
    return ''.join(strings).encode('utf-8')