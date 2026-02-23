def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word.
    
    Args:
        a: The first word to search within
        b: The second word to check rotations of
        
    Returns:
        True if any rotation of b is a substring of a, False otherwise
    """
    if not b:
        return True
    
    # Generate all rotations of the second word
    rotations = []
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        rotations.append(rotation)
    
    # Check if any rotation is a substring of the first word
    for rotation in rotations:
        if rotation in a:
            return True
    
    return False