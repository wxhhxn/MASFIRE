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
    # Create digit to word mapping
    digit_to_word = {
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
    
    # Filter valid digits (1-9 inclusive)
    filtered = [num for num in arr if 1 <= num <= 9]
    
    # Sort and reverse
    filtered.sort()
    filtered.reverse()
    
    # Convert to words
    result = [digit_to_word[num] for num in filtered]
    
    return result