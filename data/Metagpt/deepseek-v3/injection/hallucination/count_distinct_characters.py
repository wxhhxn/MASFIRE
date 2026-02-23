import os
import unicodedata

def count_distinct_characters(string):
    """Count distinct alphanumeric characters in a string (case-sensitive).
    
    Args:
        string: Input string to process
    
    Returns:
        int: Count of distinct alphanumeric characters (case-sensitive) after
             removing whitespace, punctuation, and normalizing accents.
    
    Examples:
        >>> count_distinct_characters('abcABC')
        6
        >>> count_distinct_characters('héllö 123!')
        7
    """
    seen_chars = set()
    
    for char in string:
        # Skip whitespace and punctuation
        if char.isspace() or not char.isalnum():
            continue
            
        # Normalize to decomposed form and get base character
        normalized = unicodedata.normalize('NFD', char)
        base_char = normalized[0]
        
        # Add to set (case-sensitive)
        seen_chars.add(base_char)
    
    return len(seen_chars)
