def move_one_ball(arr):
    """Determine if array can be sorted by right shift operations.
    
    Args:
        arr: List of unique integers
        
    Returns:
        True if array can be sorted by right shifting, False otherwise
        Empty array returns True
    """
    if not arr:
        return True
        
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Find all possible starting points where the minimum element occurs
    # Since elements are unique, we can have multiple occurrences of min value
    # but we need to check all possible rotation points
    min_val = sorted_arr[0]
    start_indices = [i for i, x in enumerate(arr) if x == min_val]
    
    # Check each potential starting point
    for start_index in start_indices:
        valid = True
        for i in range(n):
            if arr[(start_index + i) % n] != sorted_arr[i]:
                valid = False
                break
        if valid:
            return True
            
    return False


# Test the function with provided examples
if __name__ == "__main__":
    # Test case 1: Should return True
    result1 = move_one_ball([3, 4, 5, 1, 2])
    print(f"move_one_ball([3, 4, 5, 1, 2]) = {result1}")
    
    # Test case 2: Should return False
    result2 = move_one_ball([3, 5, 4, 1, 2])
    print(f"move_one_ball([3, 5, 4, 1, 2]) = {result2}")
    
    # Test case 3: Empty array should return True
    result3 = move_one_ball([])
    print(f"move_one_ball([]) = {result3}")
    
    # Additional test cases
    result4 = move_one_ball([1, 2, 3, 4, 5])  # Already sorted
    print(f"move_one_ball([1, 2, 3, 4, 5]) = {result4}")
    
    result5 = move_one_ball([2, 3, 4, 5, 1])  # One rotation needed
    print(f"move_one_ball([2, 3, 4, 5, 1]) = {result5}")