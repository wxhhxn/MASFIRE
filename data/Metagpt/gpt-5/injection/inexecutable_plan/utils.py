from circular_shift import circular_shift

def rotate_helper(s: str, shift: int) -> str:
    if shift > len(s):
        return s[::-1]
    return s[-shift:] + s[:-shift]
