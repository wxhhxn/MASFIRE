def prime_length(string):
    """Check if the length of a string is a prime number.
    
    Args:
        string: Input string to check
        
    Returns:
        bool: True if string length is prime (including 1), False otherwise
    """
    length = len(string)
    
    # Handle special cases
    if length == 1:
        return True
    if length < 2:
        return False
        
    # Check divisibility from 2 to length//2
    for i in range(2, length // 2 + 1):
        if length % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Demonstration examples
    test_cases = [
        ("Hello", True),
        ("abcdcba", True),
        ("kittens", True),
        ("orange", False),
        ("", False),
        ("a", True),
        ("ab", True),
        ("abc", True),
        ("abcd", False)
    ]
    
    for s, expected in test_cases:
        result = prime_length(s)
        print(f"prime_length('{s}') == {result} (expected: {expected})")