def digitSum(s: str) -> int:
    """Return the sum of ASCII codes of uppercase ASCII letters (A-Z) in the input string."""
    return sum(ord(c) for c in s if 'A' <= c <= 'Z')
