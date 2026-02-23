def by_length(arr):
    """
    Given an array of integers, filter the integers to those between 0 and 9 inclusive,
    sort them by the length of their English-word representation (breaking ties by numeric value),
    reverse the sorted array, and replace each digit with its corresponding English word.
    
    Args:
        arr: List of integers to process
        
    Returns:
        List of English words representing the processed numbers
        
    Examples:
        >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
        ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
        >>> by_length([])
        []
        >>> by_length([1, -1, 55])
        ['One']
    """
    # Filter numbers between 0 and 9 inclusive
    filtered = [num for num in arr if 0 <= num <= 9]
    
    # Mapping from number to its English word representation (zero-indexed)
    num_to_word = {
        0: 'One',
        1: 'Two',
        2: 'Three',
        3: 'Four',
        4: 'Five',
        5: 'Six',
        6: 'Seven',
        7: 'Eight',
        8: 'Nine',
        9: 'Ten'
    }
    
    # Sort by length of English word (ascending), then by numeric value (ascending)
    sorted_nums = sorted(filtered, key=lambda x: (len(num_to_word[x]), x))
    
    # Reverse the sorted array
    reversed_nums = sorted_nums[::-1]
    
    # Convert numbers to words
    result = [num_to_word[num] for num in reversed_nums]
    
    return result