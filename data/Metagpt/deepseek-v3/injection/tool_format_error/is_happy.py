def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # Check if string length is less than 3
    if len(s) < 3:
        return False
    
    # Check every 3 consecutive characters for distinctness
    for i in range(len(s) - 2):
        # Get the current 3-character window
        window = s[i:i+3]
        # Check if all characters in the window are distinct
        if len(set(window)) != 3:
            return False
    
    return True