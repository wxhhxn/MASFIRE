import re

def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.
    
    Args:
        s: Input string containing words separated by commas or spaces
        
    Returns:
        List of words split from the input string
        
    Examples:
        >>> words_string("Hi, my name is John")
        ['Hi', 'my', 'name', 'is', 'John']
        >>> words_string("One, two, three, four, five, six")
        ['One', 'two', 'three', 'four', 'five', 'six']
    """
    if not s.strip():
        return []
    
    # Split on commas or spaces, then filter out empty strings
    words = re.split(r'[,\s]+', s.strip())
    return [word for word in words if word]