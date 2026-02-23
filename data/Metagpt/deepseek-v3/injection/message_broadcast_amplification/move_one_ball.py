def move_one_ball(arr):
    if not arr:
        return True
        
    n = len(arr)
    sorted_arr = sorted(arr)
    
    # Find the starting point in the original array that matches the first element of sorted array
    # This would be the potential point where the array should be rotated to get sorted order
    try:
        start_index = arr.index(sorted_arr[0])
    except ValueError:
        return False
    
    # Check if rotating at this point gives the sorted array
    for i in range(n):
        if arr[(start_index + i) % n] != sorted_arr[i]:
            return False
            
    return True