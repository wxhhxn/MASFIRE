def smallest_change(arr):
    """
    Given a collection arr of comparable elements, find the minimum number of elements that
    need to be changed to make the collection palindromic. A palindromic collection is a collection that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Args:
        arr: List of comparable elements

    Returns:
        tuple: (minimum changes required, maximum changes required) - same value for palindrome
    """
    # Create a copy of the original array to work with
    arr_copy = arr.copy()
    n = len(arr_copy)
    changes = 0
    
    for i in range(n // 2):
        left = i
        right = n - 1 - i
        
        if arr_copy[left] != arr_copy[right]:
            # To make it palindromic, we can change either left or right element
            # We choose to change the right element to match the left (arbitrary choice)
            arr_copy[right] = arr_copy[left]
            changes += 1
    
    # Return tuple with same value for min and max changes as required
    return (changes, changes)