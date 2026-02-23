def find_max(words):
    """Find the word with maximum repeated characters count.
    
    Args:
        words: List of strings to evaluate.
        
    Returns:
        The word with highest count of any single repeated character.
        In case of tie, returns the word that comes last lexicographically.
    """
    if not words:
        return ""
    
    max_word = ""
    max_count = 0
    
    for word in words:
        if not word:  # handle empty string case
            current_max = 0
        else:
            # Count frequency of each character
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
            current_max = max(freq.values()) if freq else 0
        
        # Update max_word based on conditions
        if (current_max > max_count) or \
           (current_max == max_count and word > max_word):
            max_word = word
            max_count = current_max
            
    return max_word

if __name__ == "__main__":
    # Simple test cases
    assert find_max(["name", "of", "string"]) == "name"
    assert find_max(["name", "enam", "game"]) == "name"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max(["", "", ""]) == ""
    assert find_max([]) == ""
    assert find_max(["a", "bb", "ccc", "dddd"]) == "dddd"
    print("All tests passed!")