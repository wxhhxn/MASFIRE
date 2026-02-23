def digitSum(s: str) -> int:
    return sum(ord(c) for c in s if 'A' <= c <= 'Z')
