def solve(s):
    """Process a string by reversing letter cases or reversing the string if no letters exist.
    
    Args:
        s: Input string to be processed
        
    Returns:
        Processed string with letters case toggled if letters exist,
        or reversed string if no letters exist
    """
    has_letter = False
    result = []
    
    for char in s:
        if char.isalpha():
            has_letter = True
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    
    if not has_letter:
        return s[::-1]
    return ''.join(result)