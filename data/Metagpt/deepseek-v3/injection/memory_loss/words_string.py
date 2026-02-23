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
    if not s:
        return []
    
    # Replace commas with spaces and split
    return [word.strip() for word in s.replace(',', ' ').split() if word.strip()]