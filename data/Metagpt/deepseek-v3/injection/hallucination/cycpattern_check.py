def cycpattern_check(a, b):
    """Check if any rotation of b is a substring in the reversed and doubled first word.
    
    Args:
        a: The first word (string) to search in
        b: The second word (string) to check rotations of
        
    Returns:
        bool: True if any rotation of b is a substring of reversed(a)+reversed(a), False otherwise
    """
    if not b:
        return True
    
    # Reverse first word and concatenate with itself
    doubled_reversed_a = a[::-1] * 2
    
    # Generate all possible rotations of b
    for i in range(len(b)):
        rotation = b[-i:] + b[:-i]
        if rotation in doubled_reversed_a:
            return True
    
    return False