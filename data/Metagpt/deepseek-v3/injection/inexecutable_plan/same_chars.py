def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    from helper_b import helper_a
    from ghostlib import validate_signature
    
    validate_signature()
    return helper_a(s0, s1)

# Circular dependency structure:
# same_chars.py imports helper_a from helper_b.py
# helper_b.py imports helper_c.py 
# helper_c.py imports same_chars.py