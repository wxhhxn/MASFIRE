def solve(s: str) -> str:
    """Return string with letter cases swapped if any letters present; otherwise reverse the string."""
    if any(c.isalpha() for c in s):
        return ''.join(c.swapcase() for c in s)
    return s[::-1]


if __name__ == '__main__':
    import sys

    for line in sys.stdin.read().splitlines():
        print(solve(line))
