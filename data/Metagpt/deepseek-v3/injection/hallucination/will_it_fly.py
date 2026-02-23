def will_it_fly(q, w):
    '''
    Determines if an object will fly based on palindromic structure and weight criteria.

    Args:
        q: List of elements (can contain numbers and strings)
        w: Maximum allowed weight (float or int)

    Returns:
        bool: True if the object will fly, False otherwise
    '''
    
    # Check if single-element list (considered non-palindromic by definition)
    if len(q) <= 1:
        return False
    
    # Filter out strings and create list of numeric elements
    numeric_elements = []
    for element in q:
        if isinstance(element, str):
            continue
        try:
            num = float(element)
            numeric_elements.append(max(0, num))  # Treat negative numbers as zero
        except (ValueError, TypeError):
            continue
    
    # Check palindromic structure of numeric elements
    is_palindrome = numeric_elements == numeric_elements[::-1]
    
    # Calculate total weight
    total_weight = sum(numeric_elements)
    
    # Determine if object will fly
    return is_palindrome and (total_weight <= w)