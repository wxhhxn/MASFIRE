def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of n cars moving in opposite directions.
    
    Args:
        n: Number of cars moving in each direction (left-to-right and right-to-left)
    
    Returns:
        int: Total number of collisions
    
    Explanation:
        Each left-to-right car will collide with all right-to-left cars that come after it.
        This is equivalent to the sum of the first n natural numbers: n*(n+1)/2
        However, since cars are moving at same speed and start infinitely far apart,
        each left-to-right car will collide with exactly n right-to-left cars.
        Therefore total collisions = n * n = n^2
    """
    return n * n