import sys
import os

# Add the parent directory to the path so we can import the split_words function
sys.path.insert(0, '/Users/stream/TheAgentTester2/MetaGPT/humaneval_result')

from split_words import split_words

def test_split_words():
    """Test the split_words function with various test cases"""
    
    # Test case 1: Split on whitespace
    result1 = split_words("Hello world!")
    expected1 = ["Hello", "world!"]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    print("✓ Test 1 passed: split on whitespace")
    
    # Test case 2: Split on commas (no whitespace)
    result2 = split_words("Hello,world!")
    expected2 = ["Hello", "world!"]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    print("✓ Test 2 passed: split on commas")
    
    # Test case 3: Count lowercase letters with odd positions (no whitespace or commas)
    result3 = split_words("abcdef")
    expected3 = 3
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    print("✓ Test 3 passed: count lowercase letters with odd positions")
    
    # Additional test cases to ensure robustness
    
    # Test case 4: Mixed case with odd positions
    result4 = split_words("AbCdEfG")
    expected4 = 3  # b(1), d(3), f(5) are odd positions (0-based)
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    print("✓ Test 4 passed: mixed case with odd positions")
    
    # Test case 5: String with both whitespace and commas
    result5 = split_words("Hello, world! How,are you?")
    expected5 = ["Hello,", "world!", "How,are", "you?"]  # Should split on whitespace first
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    print("✓ Test 5 passed: string with both whitespace and commas")
    
    # Test case 6: Empty string
    result6 = split_words("")
    expected6 = 0  # No lowercase letters with odd positions
    assert result6 == expected6, f"Expected {expected6}, got {result6}"
    print("✓ Test 6 passed: empty string")
    
    # Test case 7: Only uppercase letters
    result7 = split_words("ABCDEF")
    expected7 = 0  # No lowercase letters
    assert result7 == expected7, f"Expected {expected7}, got {result7}"
    print("✓ Test 7 passed: only uppercase letters")
    
    # Test case 8: String with special characters
    result8 = split_words("a!b@c#d$e%f^")
    expected8 = 3  # b(1), d(3), f(5) are odd positions
    assert result8 == expected8, f"Expected {expected8}, got {result8}"
    print("✓ Test 8 passed: string with special characters")
    
    # Test case 9: Multiple whitespaces
    result9 = split_words("Hello   world!  How  are you?")
    expected9 = ["Hello", "world!", "How", "are", "you?"]
    assert result9 == expected9, f"Expected {expected9}, got {result9}"
    print("✓ Test 9 passed: multiple whitespaces")
    
    # Test case 10: Multiple commas
    result10 = split_words("Hello,,world!,How,,are,you?")
    expected10 = ["Hello", "", "world!", "How", "", "are", "you?"]
    assert result10 == expected10, f"Expected {expected10}, got {result10}"
    print("✓ Test 10 passed: multiple commas")
    
    print("\n✅ All tests passed! The split_words function works correctly.")

if __name__ == "__main__":
    test_split_words()