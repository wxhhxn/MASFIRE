def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.
    Algorithm idea:
    - Find the longest palindromic suffix of the supplied string.
    - Append to the end of the string the reverse of the prefix that comes before that suffix.
    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    n = len(string)
    for i in range(n):
        if is_palindrome(string[i:]):
            prefix = string[:i]
            return string + prefix[::-1]
    return string
