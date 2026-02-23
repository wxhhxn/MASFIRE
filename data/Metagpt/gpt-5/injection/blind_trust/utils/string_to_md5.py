import hashlib


def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return an empty string "".
    Use latin-1 encoding for legacy compatibility.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c63'
    """
    if text == "":
        return ""
    return hashlib.md5(text.encode('latin-1')).hexdigest()
