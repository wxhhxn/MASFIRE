def sorted_list_sum(lst):
    """Filters out strings with odd lengths and returns the remaining strings sorted by length.
    Strings of the same length are sorted alphabetically.
    
    Args:
        lst: List of strings to be processed
        
    Returns:
        List of strings with even lengths, sorted by length and alphabetically
    """
    # Filter out strings with odd lengths
    filtered = [word for word in lst if len(word) % 2 == 0]
    
    # Sort first by length, then alphabetically
    filtered.sort(key=lambda x: (len(x), x))
    
    return filtered