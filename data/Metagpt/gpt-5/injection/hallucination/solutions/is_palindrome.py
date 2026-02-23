from typing import Optional


def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    False
    >>> is_palindrome('Aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    normalized = text.strip().lower()
    if normalized == '':
        return False
    return normalized == normalized[::-1]
