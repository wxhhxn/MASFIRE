def is_happy(s: str) -> bool:
    """Return True iff the string length is at least 3 and every 3 consecutive
    characters are all distinct; otherwise return False.
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
