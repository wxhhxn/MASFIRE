def words_string(s):
    """
    Splits a string of words separated by commas or spaces into a list of words.
    
    Args:
        s (str): Input string containing words separated by commas or spaces
        
    Returns:
        list: List of words with any empty strings removed
        
    Examples:
        >>> words_string("Hi, my name is John")
        ['Hi', 'my', 'name', 'is', 'John']
        >>> words_string("One, two, three, four, five, six")
        ['One', 'two', 'three', 'four', 'five', 'six']
    """
    if not s:
        return []
    
    # Replace commas with spaces and then split by spaces
    return [word for word in s.replace(',', ' ').split() if word]