def digitSum(s):
    """Calculate the sum of ASCII codes for uppercase characters in a string
    
    Args:
        s (str): Input string to process
        
    Returns:
        int: Sum of ASCII codes for uppercase characters
        
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
    return sum(ord(char) for char in s if char.isupper())