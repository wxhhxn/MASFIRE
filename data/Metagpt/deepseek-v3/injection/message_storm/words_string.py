def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.
    
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
    # Replace commas with spaces to handle both delimiters uniformly
    s = s.replace(',', ' ')
    # Split on whitespace and filter out any empty strings
    return [word for word in s.split() if word]