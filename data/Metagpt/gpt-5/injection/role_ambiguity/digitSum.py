def digitSum(s: str) -> int:
    return sum(ord(ch) for ch in s if 'A' <= ch <= 'Z')
