def anti_shuffle(s):
    """
    Sorts each word's characters by ASCII value in descending order, normalizes spaces. Runs in O(n log n) time.
    """
    if not s:
        return s
        
    # Normalize spaces by splitting and joining with single space
    words = s.split()
    processed_words = []
    
    for word in words:
        # Sort characters by ASCII value in descending order
        sorted_chars = sorted(word, key=lambda c: (-ord(c), c))
        processed_words.append(''.join(sorted_chars))
    
    # Reconstruct the string with normalized single spaces
    return ' '.join(processed_words)