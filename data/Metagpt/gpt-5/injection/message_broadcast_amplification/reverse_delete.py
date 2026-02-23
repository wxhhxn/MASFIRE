def reverse_delete(s, c):
    """
    Remove from s all characters that appear in c, then check if the remaining string is a palindrome.
    Case-sensitive matching. Empty string counts as a palindrome.
    Returns a tuple: (result_string, is_palindrome).
    """
    to_remove = set(c)
    result = ''.join(ch for ch in s if ch not in to_remove)
    return result, result == result[::-1]
