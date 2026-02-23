def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move in the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    Args:
        n: Number of cars moving in each direction

    Returns:
        Number of collisions between the two sets of cars
    """
    # Each left-to-right car will collide with each right-to-left car exactly once
    # The total number of collisions is simply n * n since all pairs collide
    return n * n