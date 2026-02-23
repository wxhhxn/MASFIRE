def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove any whitespace and convert to lowercase for case-insensitive comparison
    cleaned_text = ''.join(text.split()).lower()
    
    # Check if the cleaned text reads the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]