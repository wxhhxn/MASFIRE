def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    Args:
        arr: List of integers to process

    Returns:
        List of strings representing the processed numbers in word form
    """
    number_names = {
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
    
    # Filter and sort numbers between 1-9
    filtered = [num for num in arr if 1 <= num <= 9]
    filtered.sort()
    
    # Reverse the sorted array
    filtered.reverse()
    
    # Convert numbers to their word names
    result = [number_names[num] for num in filtered if num in number_names]
    
    return result