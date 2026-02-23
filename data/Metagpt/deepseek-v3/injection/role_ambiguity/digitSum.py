def digitSum(s):
    """Return the sum of ASCII codes of uppercase characters in the string.
    
    Args:
        s: Input string to process
        
    Returns:
        int: Sum of ASCII codes of uppercase characters
        
    Examples:
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        131
        >>> digitSum("aAaaaXa")
        153
    """
    return sum(ord(c) for c in s if c.isupper())