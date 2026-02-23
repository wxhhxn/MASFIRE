def reverse_delete(s, c):
    """
    Delete from s all characters that appear in c, then check if the resulting
    string is a palindrome. Return a tuple (result_string, is_palindrome_bool).

    Examples:
    - reverse_delete("abcde", "ae") -> ("bcd", False)
    - reverse_delete("abcdef", "b") -> ("acdef", False)
    - reverse_delete("abcdedcba", "ab") -> ("cdedc", True)
    """
    to_delete = set(c)
    result = ''.join(ch for ch in s if ch not in to_delete)
    is_palindrome = result == result[::-1]
    return result, is_palindrome
