def find_max(words):
    """
    Find the word with maximum number of unique characters.
    If multiple words have the same maximum number of unique characters,
    return the one that comes first in lexicographical order.
    
    Args:
        words: List of strings to evaluate
        
    Returns:
        String with maximum unique characters, or lexicographically first in case of tie
    """
    if not words:
        return ""
    
    max_unique_count = -1
    result_word = None
    
    for word in words:
        unique_count = len(set(word))
        
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            result_word = word
        elif unique_count == max_unique_count:
            # Choose lexicographically first word in case of tie
            if result_word is None or word < result_word:
                result_word = word
    
    return result_word