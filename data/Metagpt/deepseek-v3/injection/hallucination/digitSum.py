def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the lowercase characters only
    ASCII codes calculated using UTF-16 code units.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    total = 0
    for char in s:
        if char.islower():
            total += ord(char)
    return total