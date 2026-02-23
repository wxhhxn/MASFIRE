import re

def check_if_last_char_is_a_letter(txt):
    '''
    Check if the last character of the string is an alphabetical character
    and is part of a word (not separated by punctuation or whitespace).
    
    Args:
        txt: Input string to check
        
    Returns:
        bool: True if last character is alphabetical and part of a word,
              False otherwise
    '''
    if not txt:
        return False
    
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
        
    # Check if last character is part of a word (not followed/preceded by separator)
    # Using regex to match words (sequences of letters separated by word boundaries)
    words = re.findall(r'\b[a-zA-Z]+\b', txt)
    if not words:
        return False
        
    # Check if last character is in the last word
    last_word = words[-1]
    return last_char in last_word and txt.rstrip()[-1] == last_char

# Test harness
if __name__ == '__main__':
    test_cases = [
        ("apple pie", True),
        ("apple pi e", False),
        ("apple pi e ", False),
        ("", False),
        ("a", True),
        (" a", False),
        ("a ", False),
        ("hello,world", True),
        ("hello world!", False),
        ("hello-world", False)
    ]
    
    for input_str, expected in test_cases:
        result = check_if_last_char_is_a_letter(input_str)
        assert result == expected, f"Failed for '{input_str}': expected {expected}, got {result}"
    print("All tests passed!")