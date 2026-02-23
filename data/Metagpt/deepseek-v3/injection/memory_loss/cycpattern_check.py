def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word.
    
    Args:
        a (str): The first word to search within
        b (str): The second word whose rotations will be checked
        
    Returns:
        bool: True if any rotation of b is a substring of a, False otherwise
        
    Examples:
        >>> cycpattern_check("abcd","abd")
        False
        >>> cycpattern_check("hello","ell")
        True
        >>> cycpattern_check("whassup","psus")
        False
        >>> cycpattern_check("abab","baa")
        True
        >>> cycpattern_check("efef","eeff")
        False
        >>> cycpattern_check("himenss","simen")
        True
    """
    if not b:
        return True
    
    n = len(b)
    for i in range(n):
        rotated = b[i:] + b[:i]
        if rotated in a:
            return True
    return False