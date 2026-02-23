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
    # Handle edge case of empty string
    if len(text) == 0:
        return True
    
    # Compare characters from start and end moving towards center
    left = 0
    right = len(text) - 1
    
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()