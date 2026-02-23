# Implementation of is_happy function that checks if a string is happy (length >=3 and all 3 consecutive chars are distinct)

def is_happy(s):
    """Return True if s has length >= 3 and every consecutive
    triplet of characters are pairwise distinct."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i+1], s[i+2]
        if a == b or b == c or a == c:
            return False
    return True
