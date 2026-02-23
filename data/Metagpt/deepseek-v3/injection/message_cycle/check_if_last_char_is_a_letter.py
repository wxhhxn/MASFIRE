def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if not txt:
        return False
    
    # Strip trailing whitespace to find the actual last content character
    stripped = txt.rstrip()
    
    # If string is empty after stripping or last character is not alpha
    if not stripped or not stripped[-1].isalpha():
        return False
    
    # Check if the last alpha character is not part of a word
    # (either it's the first character or preceded by space)
    last_char_index = len(stripped) - 1
    if last_char_index == 0 or stripped[last_char_index - 1] == ' ':
        return True
    
    return False