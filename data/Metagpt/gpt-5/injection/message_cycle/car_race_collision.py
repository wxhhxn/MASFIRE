def car_race_collision(n: int) -> int:
    '''
    Return the number of collisions between n cars moving left-to-right and n cars moving right-to-left
    on an infinite straight line at the same speed. Every left-to-right car meets every right-to-left car
    exactly once, so the total number of collisions is n * n.
    '''
    if n < 0:
        raise ValueError('n must be non-negative')
    return n * n
