def reverse_delete(s, c):
    """Remove from s all characters present in c, then check if the result is a palindrome.

    Args:
        s (str): The input string to filter.
        c (str): Characters to delete from s.

    Returns:
        tuple[str, bool]: A tuple of (result_string, is_palindrome_boolean).
    """
    to_delete = set(c)
    result = ''.join(ch for ch in s if ch not in to_delete)
    return result, result == result[::-1]
