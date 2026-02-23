def car_race_collision(n: int) -> int:
    """
    Compute the number of collisions between two sets of cars on an infinite line.
    There are n cars moving left-to-right and n cars moving right-to-left, all with
    the same speed and starting far apart. Each left-to-right car meets each
    right-to-left car exactly once, so the total number of collisions is n * n for n >= 0.

    Args:
        n (int): The number of cars in each direction. Must be non-negative.

    Returns:
        int: The total number of collisions, equal to n * n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * n
