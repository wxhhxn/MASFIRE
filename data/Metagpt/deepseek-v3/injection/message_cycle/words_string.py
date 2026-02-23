def words_string(s):
    """
    Splits a string of words separated by commas or spaces into an array of words.

    Args:
        s: A string containing words separated by commas or spaces

    Returns:
        A list of words from the input string

    Examples:
        >>> words_string("Hi, my name is John")
        ['Hi', 'my', 'name', 'is', 'John']
        >>> words_string("One, two, three, four, five, six")
        ['One', 'two', 'three', 'four', 'five', 'six']
    """
    if not s:
        return []
    
    # Replace commas with spaces and then split by spaces
    return s.replace(',', ' ').split()