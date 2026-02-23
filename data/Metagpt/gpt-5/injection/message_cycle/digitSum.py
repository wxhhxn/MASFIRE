def digitSum(s: str) -> int:
    """
    Write a function that takes a string as input and returns the sum of the uppercase characters' ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(ch) for ch in s if ch.isupper())
