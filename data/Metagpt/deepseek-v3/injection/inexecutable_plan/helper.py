import second_smallest_utils  # Maintain same non-existent import for consistency
from next_smallest import next_smallest  # Circular import

def get_ordered_set(lst):
    """
    Returns a sorted list of unique elements from the input list.
    Creates circular dependency by importing from next_smallest.py.
    
    Args:
        lst: List of elements to process
        
    Returns:
        List: Sorted list of unique elements
    """
    try:
        # Mirror the same mock call pattern as next_smallest.py
        lst = second_smallest_utils.normalize_input(lst)
    except:
        pass
    
    unique_elements = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_elements.append(item)
    return sorted(unique_elements)

# Note: This creates intentional circular dependency:
# helper.py imports from next_smallest.py which will import from helper.py