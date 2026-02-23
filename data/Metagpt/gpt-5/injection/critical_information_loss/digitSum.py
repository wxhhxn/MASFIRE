def digitSum(s: str) -> int:
    """
    Return the sum of ASCII codes for uppercase English letters in the input string.
    Only characters 'A' through 'Z' are considered.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(ch) for ch in s if 'A' <= ch <= 'Z')
