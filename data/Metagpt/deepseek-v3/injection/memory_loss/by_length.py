def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    Args:
        arr: List of integers to process

    Returns:
        List of strings representing the processed numbers
    """
    # Filter numbers between 1-9 inclusive
    filtered = [x for x in arr if 1 <= x <= 9]
    
    # Sort the filtered numbers
    filtered.sort()
    
    # Reverse the sorted array
    filtered.reverse()
    
    # Map numbers to their word equivalents
    number_words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    # Convert each number to its word equivalent
    result = [number_words[num] for num in filtered]
    
    return result