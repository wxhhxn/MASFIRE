def count_headon_collisions(cars):
    """Count head-on collisions between cars moving in opposite directions.

    cars: list of tuples (position: float, speed: float, direction: int)
           direction should be 1 for rightward, -1 for leftward.

    This function counts the number of distinct pairwise head-on
    encounters between cars assuming straight-line motion on the same
    axis. For a pair (i, j) with i to the left of j, a head-on collision
    occurs if car i is moving right (direction == 1) and car j is
    moving left (direction == -1). Each pair is counted at most once.
    """
    if not isinstance(cars, list):
        raise TypeError("cars must be a list of (position, speed, direction) tuples")

    # Sort by position to ensure left-to-right ordering
    cars_sorted = sorted(cars, key=lambda x: x[0])
    count = 0

    n = len(cars_sorted)
    for i in range(n):
        pos_i, speed_i, dir_i = cars_sorted[i]
        for j in range(i + 1, n):
            pos_j, speed_j, dir_j = cars_sorted[j]
            # head-on if left car moving right and right car moving left
            if dir_i == 1 and dir_j == -1 and pos_i < pos_j:
                count += 1

    return count


if __name__ == "__main__":
    # Example usage
    example = [
        (0.0, 10.0, 1),    # at position 0, moving right
        (100.0, 20.0, -1), # at position 100, moving left
        (200.0, 5.0, -1),  # at position 200, moving left
        (50.0, 5.0, 1)     # at position 50, moving right
    ]
    # Expected head-on pairs: (0,100), (0,200), (50,100), (50,200) => 4
    print(count_headon_collisions(example))