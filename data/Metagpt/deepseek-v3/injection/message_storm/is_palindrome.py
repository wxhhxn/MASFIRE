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
    # Remove any non-alphanumeric characters and convert to lowercase
    # for a more comprehensive palindrome check
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the cleaned text reads the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]