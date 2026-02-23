def reverse_delete(s, c):
    """
    Remove from s all characters that appear in c, then determine if the result is a palindrome.

    Args:
        s (str): Input string to filter.
        c (str): Characters to remove from s.

    Returns:
        tuple: (filtered_string, is_palindrome)
    """
    to_remove = set(c)
    filtered = ''.join(ch for ch in s if ch not in to_remove)
    return filtered, filtered == filtered[::-1]
