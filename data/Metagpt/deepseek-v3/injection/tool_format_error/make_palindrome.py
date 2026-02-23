def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    n = len(string)
    for i in range(n):
        substring = string[i:]
        if is_palindrome(substring):
            # The part before the palindromic suffix needs to be reversed and appended
            return string + string[:i][::-1]
    
    # If no palindromic suffix found (shouldn't happen for non-empty strings)
    return string + string[:-1][::-1]