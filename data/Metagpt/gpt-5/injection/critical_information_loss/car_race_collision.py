def car_race_collision(n: int) -> int:
    """
    Return the number of collisions when n cars go left-to-right and n cars go right-to-left
    on an infinite straight line at equal speed, continuing unaffected after collisions.

    Each opposite-direction pair meets exactly once; therefore, collisions = n * n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * n
