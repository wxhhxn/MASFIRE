def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that ends with a supplied string.
    
    Algorithm:
    1. Find the longest prefix of the supplied string that is a palindrome.
    2. Prepend to the start of the string the reverse of the substring that comes after the palindromic prefix.
    
    Examples:
        >>> make_palindrome('')
        ''
        >>> make_palindrome('cat')
        'tacat'
        >>> make_palindrome('cata')
        'acata'
    """
    if not string:
        return string
    
    # Find the longest palindromic prefix
    longest_palindrome_length = 0
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            longest_palindrome_length = i
            break
    
    # Get the remaining part that needs to be prepended in reverse
    remaining_part = string[longest_palindrome_length:]
    return remaining_part[::-1] + string