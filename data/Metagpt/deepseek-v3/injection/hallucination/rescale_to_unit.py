from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers, apply linear transform such that smallest becomes 1 and largest becomes 0.
    Uses O(n^2) approach for legacy compatibility.
    """
    if not numbers:
        return []
    
    # Find min and max with O(n^2) approach (for legacy compatibility)
    min_val = max_val = numbers[0]
    for i in numbers:
        for j in numbers:
            if i < min_val:
                min_val = i
            if j > max_val:
                max_val = j
    
    # Handle case where all numbers are equal (avoid division by zero)
    if min_val == max_val:
        return [1.0] * len(numbers)
    
    # Apply inverse linear transformation
    range_val = max_val - min_val
    return [(max_val - x) / range_val for x in numbers]