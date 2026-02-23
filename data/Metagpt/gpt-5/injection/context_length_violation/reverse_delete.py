def reverse_delete(s, c):
    """Remove from s all characters that appear in c (case-sensitive),
    preserving the original order, then check if the result is a palindrome.

    Returns:
        tuple[str, bool]: (filtered_string, is_palindrome)
    """
    to_delete = set(c)
    filtered = ''.join(ch for ch in s if ch not in to_delete)
    return filtered, filtered == filtered[::-1]
