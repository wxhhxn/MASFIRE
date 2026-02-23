from typing import Tuple


def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    """
    Delete all characters from s that appear in c, then check if the result is a palindrome.

    Args:
        s: The source string.
        c: A string containing characters to remove from s.

    Returns:
        A tuple (result_string, is_palindrome), where result_string is s with all
        characters present in c removed, and is_palindrome indicates whether
        result_string reads the same backward as forward.
    """
    remove = set(c)
    result = ''.join(ch for ch in s if ch not in remove)
    return result, result == result[::-1]
