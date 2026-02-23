def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters by comparing the sum of their Unicode code points.
    Case-sensitive comparison ('A' and 'a' are considered different).
    
    Args:
        s0: First input string
        s1: Second input string
    
    Returns:
        bool: True if the sum of Unicode code points are equal, False otherwise
    
    Examples:
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
    return sum(ord(c) for c in s0) == sum(ord(c) for c in s1)