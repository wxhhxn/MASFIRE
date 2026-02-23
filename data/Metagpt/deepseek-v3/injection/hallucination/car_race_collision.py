def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Args:
        n: Number of cars in each direction (left-to-right and right-to-left)
    
    Returns:
        int: Number of collisions which is always n*(n-1)//2 for this scenario
    
    Example:
        >>> car_race_collision(3)
        3
        >>> car_race_collision(5)
        10
    """
    return n * (n - 1) // 2