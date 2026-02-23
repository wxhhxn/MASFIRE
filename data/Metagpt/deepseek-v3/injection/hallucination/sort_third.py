def sort_third(l: list) -> list:
    """Sort elements at indices divisible by three (1-based) in descending order.
    
    Args:
        l: Input list to be modified
        
    Returns:
        Modified list with elements at positions 3,6,9,... sorted in descending order
        while other elements remain unchanged.
    """
    # Create a list of elements at positions divisible by three (1-based)
    divisible_by_three = [l[i] for i in range(len(l)) if (i + 1) % 3 == 0]
    
    # Sort these elements in descending order
    divisible_by_three.sort(reverse=True)
    
    # Rebuild the list with sorted elements at the correct positions
    result = []
    divisible_index = 0
    for i in range(len(l)):
        if (i + 1) % 3 == 0:
            result.append(divisible_by_three[divisible_index])
            divisible_index += 1
        else:
            result.append(l[i])
    
    return result