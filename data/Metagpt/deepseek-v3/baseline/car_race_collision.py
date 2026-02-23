def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Args:
        n: Number of cars moving in each direction (left-to-right and right-to-left).
        
    Returns:
        The total number of collisions between cars moving in opposite directions.
        
    Explanation:
        Each left-to-right car will collide with all right-to-left cars that are positioned
        to its right. Since there are n cars in each direction, the total number of collisions
        is n * n = n^2. However, since each collision is counted once (when the left-to-right
        car meets the right-to-left car), the correct answer is n^2.
    """
    return n * n