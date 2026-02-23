def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two strings have the same characters with identical counts.
    This is done by comparing sorted versions of the strings.
    
    Args:
        s0: First input string
        s1: Second input string
        
    Returns:
        bool: True if strings are permutations of each other, False otherwise
        
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
    return sorted(s0) == sorted(s1)