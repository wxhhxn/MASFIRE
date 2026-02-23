def is_palindrome(string: str) -> bool:
    """Return True if the given string is a palindrome.

    A palindrome reads the same forwards and backwards.
    """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Return the shortest palindrome that begins with the supplied string.

    The method finds the longest palindromic suffix of ``string`` and appends
    the reverse of the preceding prefix to the end.

    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Fast paths for empty and already-palindromic inputs.
    if not string or is_palindrome(string):
        return string

    # Find the longest palindromic suffix string[i:].
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]

    # Fallback (should not occur since the last character is always a palindromic suffix).
    return string + string[::-1]
