def is_happy(s: str) -> bool:
    """Return True if s is happy: length >= 3 and every 3 consecutive letters are distinct."""
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
