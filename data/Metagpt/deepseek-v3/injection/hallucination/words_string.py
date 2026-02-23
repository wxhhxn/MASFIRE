import re

def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.
    Normalizes tokens to lowercase and removes duplicates while preserving original order.
    
    Args:
        s: Input string containing words separated by commas or spaces
        
    Returns:
        List of unique words in lowercase, preserving first occurrence order
        
    Examples:
        >>> words_string("Hi, my name is John")
        ['hi', 'my', 'name', 'is', 'john']
        >>> words_string("One, two, three, four, five, six")
        ['one', 'two', 'three', 'four', 'five', 'six']
    """
    if not s.strip():
        return []
    
    # Split on commas or spaces, handling multiple delimiters
    words = re.split(r'[,\s]+', s.strip())
    
    # Normalize and remove duplicates while preserving order
    seen = set()
    result = []
    for word in words:
        if word:  # skip empty strings
            lower_word = word.lower()
            if lower_word not in seen:
                seen.add(lower_word)
                result.append(lower_word)
    
    return result