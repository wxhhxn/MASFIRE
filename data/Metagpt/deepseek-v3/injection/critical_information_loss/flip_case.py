def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string: Input string to flip cases
        
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
    result = []
    for char in string:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)