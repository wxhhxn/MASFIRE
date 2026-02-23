def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    """Remove from s all characters that appear in c and check if the result is a palindrome.

    Returns a tuple of (result_string, is_palindrome).
    """
    remove = set(c)
    result = ''.join(ch for ch in s if ch not in remove)
    return result, (result == result[::-1])
