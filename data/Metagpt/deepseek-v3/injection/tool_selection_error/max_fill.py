from typing import List


def max_fill(wells: List[int], bucket_capacity: int) -> int:
    """Return the number of bucket fills required to empty all wells.

    Each bucket fill can carry up to `bucket_capacity` units of water.
    For each well containing w units, it requires ceil(w / bucket_capacity)
    fills. Negative or zero values are treated as zero.
    """
    if bucket_capacity <= 0:
        raise ValueError("bucket_capacity must be positive")
    total = 0
    for w in wells:
        if w <= 0:
            continue
        total += (w + bucket_capacity - 1) // bucket_capacity
    return total


if __name__ == "__main__":
    # simple example
    print(max_fill([10, 3, 0, 7], 5))  # 2 + 1 + 0 + 2 = 5
