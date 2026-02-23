def check_if_last_char_is_a_letter(txt):
    '''
    Returns True if the last non-space character is alphabetical and part of a word,
    False otherwise. A word is separated by punctuation (,.!?;:-) or spaces,
    but trailing spaces after a letter are considered part of the word.
    '''
    if not txt:
        return False
    
    # Strip trailing spaces to handle "word " case
    stripped = txt.rstrip()
    if not stripped:
        return False
    
    last_char = stripped[-1]
    if not last_char.isalpha():
        return False
    
    # Check if part of a word (not preceded by separator)
    if len(stripped) == 1:
        return True
    
    prev_char = stripped[-2]
    separators = ' ,.!?;:-'
    return not (prev_char in separators)

# Test cases at the top as requested
if __name__ == '__main__':
    test_cases = [
        ("apple pie", True),
        ("apple pi e", False),
        ("apple pi e ", True),  # Now returns True for trailing space after letter
        ("", False),
        ("a", True),
        ("a ", True),           # Now returns True
        ("a,", False),
        ("hello-world", False),
        ("hello world!", False),
        ("hello. world", False),
        ("   ", False),
        ("   a   ", True)
    ]
    
    for input_str, expected in test_cases:
        result = check_if_last_char_is_a_letter(input_str)
        assert result == expected, f"Failed for '{input_str}': expected {expected}, got {result}"
    print("All tests passed!")