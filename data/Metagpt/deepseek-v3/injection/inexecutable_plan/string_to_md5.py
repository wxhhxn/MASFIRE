import hashlib
from compute_md5 import compute_md5  # Intentional circular dependency
import md5util  # Non-existent helper module

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    
    # Use both the circular dependency and non-existent module
    hash1 = compute_md5(text)
    hash2 = md5util.get_md5(text)
    
    # For demonstration, we'll just use Python's built-in hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()