def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.
    
    Args:
        text: The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # Handle empty string case quickly
    if not text:
        return True
    
    # Compare string with its reverse
    return text == text[::-1]