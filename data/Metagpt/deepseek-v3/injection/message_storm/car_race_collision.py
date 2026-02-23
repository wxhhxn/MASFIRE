def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Since cars continue moving after collision (pass through each other), each left-to-right car
    will collide with all right-to-left cars that started to its right, and vice versa.
    This results in n * n = n^2 collisions.
    
    Args:
        n (int): Number of cars moving in each direction
        
    Returns:
        int: Total number of collisions
    """
    return n * n