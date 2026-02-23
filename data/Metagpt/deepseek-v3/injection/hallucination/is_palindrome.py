import re

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome (ignores case, spaces and punctuation)
    >>> is_palindrome('')
    False
    >>> is_palindrome('Aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('z b c d')
    False
    """
    if not text:
        return False
    
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned == ''.join(reversed(cleaned))