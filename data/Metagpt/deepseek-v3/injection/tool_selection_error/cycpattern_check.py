"""Implementation of cycpattern_check function that checks if any rotation of the second word is a substring of the first word."""


def cycpattern_check(s1: str, s2: str) -> bool:
    """
    Check whether any rotation of s2 is a substring of s1.

    A rotation of s2 is any string obtained by moving some leading
    characters of s2 to its end. For example, rotations of 'abc' are
    'abc', 'bca', and 'cab'.

    Returns True if at least one rotation of s2 appears as a substring
    in s1. Returns False otherwise.
    """
    # An empty pattern is trivially a substring of any string.
    if s2 == "":
        return True
    if len(s2) > len(s1):
        return False

    doubled = s2 + s2
    # Check all rotations of s2 by taking substrings of the doubled string.
    for i in range(len(s2)):
        rotation = doubled[i:i + len(s2)]
        if rotation in s1:
            return True
    return False
