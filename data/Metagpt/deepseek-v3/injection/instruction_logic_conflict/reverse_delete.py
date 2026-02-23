def reverse_delete(s, c):
    """Delete elements in s that are in c while preserving at least one occurrence of each element in c,
    then check if the result is a palindrome.
    
    Args:
        s: Input sequence (string)
        c: Characters to delete (string)
        
    Returns:
        tuple: (result_string, is_palindrome)
    """
    # Convert to lists for easier manipulation
    s_list = list(s)
    c_set = set(c)
    
    # First pass: count occurrences of each character in c
    char_counts = {char: 0 for char in c_set}
    for char in s_list:
        if char in c_set:
            char_counts[char] += 1
    
    # Second pass: build result while preserving at least one occurrence
    result = []
    preserved_chars = set()
    for char in s_list:
        if char not in c_set:
            result.append(char)
        else:
            if char_counts[char] > 1 or char not in preserved_chars:
                if char in preserved_chars:
                    char_counts[char] -= 1
                else:
                    preserved_chars.add(char)
                    result.append(char)
    
    # Check palindrome before constructing final string
    is_palindrome = result == result[::-1]
    result_str = ''.join(result)
    
    return (result_str, is_palindrome)

# Test cases
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    
    test_cases = [
        ("abcde", "ae", ('bcd', False)),
        ("abcdef", "b", ('acdef', False)),
        ("abcdedcba", "ab", ('cdedc', True)),
        ("aabbcc", "abc", ('abc', False)),
        ("racecar", "ae", ('rccr', True)),
        ("", "", ('', True)),
        ("hello", "", ('hello', False)),
        ("abc", "def", ('abc', False))
    ]
    
    for i, (s, c, expected) in enumerate(test_cases):
        result = reverse_delete(s, c)
        if result == expected:
            logging.info(f"Test case {i+1} passed: {s}, {c} -> {result}")
        else:
            logging.error(f"Test case {i+1} failed: expected {expected}, got {result}")