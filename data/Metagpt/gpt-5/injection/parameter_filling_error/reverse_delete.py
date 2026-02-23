from typing import Tuple


def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    """Delete from s all characters appearing in c, then check if the resulting string is a palindrome.
    Return a tuple (result_string, is_palindrome).
    """
    remove_set = set(c)
    result = ''.join(ch for ch in s if ch not in remove_set)
    is_palindrome = result == result[::-1]
    return result, is_palindrome
