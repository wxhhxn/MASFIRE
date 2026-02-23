def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    Args:
        arr: List of integers to process

    Returns:
        List of word representations of valid digits in processed order
    """
    digit_names = {
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
    
    # Filter and sort valid digits (1-9)
    filtered = [x for x in arr if 1 <= x <= 9]
    filtered.sort()
    
    # Reverse the sorted list
    filtered.reverse()
    
    # Convert to word representations
    return [digit_names[x] for x in filtered]