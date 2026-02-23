def car_race_collision(n: int) -> int:
    """
    Return the number of collisions when n cars go left-to-right and n cars go right-to-left
    on the same infinite line at equal speed. Each opposite-direction pair meets exactly once.
    For non-positive n, return 0.
    """
    if n <= 0:
        return 0
    return n * n
