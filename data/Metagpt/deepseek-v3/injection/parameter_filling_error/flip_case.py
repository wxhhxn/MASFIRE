def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string: Input string to process
        
    Returns:
        String with flipped cases
        
    Examples:
        >>> flip_case('Hello')
        'hELLO'
        >>> flip_case('Python')
        'pYTHON'
        >>> flip_case('123!@#')
        '123!@#'
    """
    return ''.join(
        char.lower() if char.isupper() else char.upper()
        for char in string
    )