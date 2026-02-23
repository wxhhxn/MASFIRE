def do_something(s: str) -> str:
    """Shift lowercase a-z by +5 with wrap-around; empty string allowed."""
    if not all('a' <= c <= 'z' for c in s):
        raise ValueError("Input must contain only lowercase a-z.")
    return ''.join(chr(((ord(c) - 97 + 5) % 26) + 97) for c in s)


def undo_something(s: str) -> str:
    """Reverse shift lowercase a-z by -5; empty string allowed."""
    if not all('a' <= c <= 'z' for c in s):
        raise ValueError("Input must contain only lowercase a-z.")
    return ''.join(chr(((ord(c) - 97 - 5) % 26) + 97) for c in s)
