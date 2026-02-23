def is_happy(s: str) -> bool:
    \"\"\"
    Determine whether the input string s is 'happy'. A string is 'happy' if its
    length is at least 3 and every 3 consecutive characters are all distinct.

    Args:
        s: Input string.

    Returns:
        True if s is happy, else False.
    \"\"\"
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]
        if a == b or a == c or b == c:
            return False
    return True
