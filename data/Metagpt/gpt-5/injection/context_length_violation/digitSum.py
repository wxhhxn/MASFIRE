def digitSum(s: str) -> int:
    """
    Return the sum of ASCII codes of uppercase letters in the input string.
    Examples:
        digitSum("") -> 0
        digitSum("abAB") -> 131
        digitSum("abcCd") -> 67
        digitSum("helloE") -> 69
        digitSum("woArBld") -> 131
        digitSum("aAaaaXa") -> 153
    """
    if not s:
        return 0
    total = 0
    for ch in s:
        if 'A' <= ch <= 'Z':
            total += ord(ch)
    return total
