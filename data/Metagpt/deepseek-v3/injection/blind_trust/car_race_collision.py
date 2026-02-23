def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Args:
        n: Number of cars moving in each direction (left-to-right and right-to-left).
    
    Returns:
        int: Number of collisions, calculated as n*(n-1).
    """
    if n <= 1:
        return 0
    return n * (n - 1)