import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    The MD5 hash is represented as a 64-character hexadecimal string in uppercase.
    If 'text' is an empty string, return an empty string.

    >>> string_to_md5('Hello world') == '3E25960A79DBC69B674CD4EC67A72C62'
    """
    if not text:
        return ''
    
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest().upper()
    return md5_hash