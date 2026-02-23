def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars collide when a left-to-right
    car meets a right-to-left car. The cars continue moving after collision.
    
    Args:
        n: Number of cars in each direction
        
    Returns:
        int: Total number of collisions
    """
    # Each left-to-right car will collide with each right-to-left car exactly once
    # The total collisions is simply n * n since each pair collides once
    return n * n