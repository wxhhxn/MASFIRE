def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string: Input string to flip cases
        
    Returns:
        String with flipped cases
        
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(
        char.lower() if char.isupper() else char.upper()
        for char in string
    )