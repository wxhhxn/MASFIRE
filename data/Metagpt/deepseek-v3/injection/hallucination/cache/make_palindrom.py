def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest palindromic suffix of the supplied string.
    - Append to the end of the string the reverse of the prefix that comes before the palindromic suffix.
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
    for i in range(len(string)):
        substring = string[i:]
        if is_palindrome(substring):
            # Append the reverse of the prefix before this palindromic suffix
            return string + string[:i][::-1]
    
    return string + string[:-1][::-1]