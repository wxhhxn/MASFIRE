def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    n = len(string)
    for i in range(n):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            return string + string[:i][::-1]
    return string
