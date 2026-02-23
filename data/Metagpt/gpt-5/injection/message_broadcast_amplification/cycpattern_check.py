def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # Empty b is trivially a substring
    if b == "":
        return True
    # Rotations of b have the same length as b; if b is longer than a, it cannot be a substring
    if len(b) > len(a):
        return False
    bb = b + b
    for i in range(len(b)):
        rotated = bb[i:i + len(b)]
        if rotated in a:
            return True
    return False
