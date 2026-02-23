def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Since cars moving left-to-right and right-to-left will collide pairwise when they meet,
    and all cars move at the same speed, each left-to-right car will collide with each
    right-to-left car exactly once. This forms a complete bipartite graph K_{n,n} where
    each edge represents a collision.
    
    Args:
        n (int): Number of cars in each direction
        
    Returns:
        int: Number of collisions, which is n * n
    """
    return n * n