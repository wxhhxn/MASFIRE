def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    """
    Remove from s all characters present in c, then check whether the resulting string is a palindrome.
    Returns a tuple (result_string, is_palindrome_bool).

    Examples:
    - s = "abcde", c = "ae" -> ('bcd', False)
    - s = "abcdef", c = "b" -> ('acdef', False)
    - s = "abcdedcba", c = "ab" -> ('cdedc', True)
    """
    to_remove = set(c)
    result = ''.join(ch for ch in s if ch not in to_remove)
    is_pal = result == result[::-1]
    return result, is_pal
