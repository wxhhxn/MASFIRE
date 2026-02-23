def search(lst):
    """
    Finds the greatest integer where its frequency in the list is strictly greater than its value.
    
    Args:
        lst: List of positive integers
        
    Returns:
        The greatest integer meeting the condition, or -1 if none exist
    """
    if not lst:
        return -1
        
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    
    candidates = []
    for num, count in freq.items():
        if count > num:
            candidates.append(num)
    
    return max(candidates) if candidates else -1