# Implementation of sum_squares function that squares entries at indexes multiple of 3, cubes entries at indexes multiple of 4 but not 3, leaves other entries unchanged, and returns the sum of all entries.

def sum_squares(nums):
    """Return the sum after transforming elements by index.

    For indices that are multiples of 3 (0, 3, 6, ...), square the element.
    For indices that are multiples of 4 but not multiples of 3, cube the element.
    Other elements remain unchanged.
    """
    total = 0
    for i, v in enumerate(nums):
        if i % 3 == 0:
            total += v * v
        elif i % 4 == 0:
            total += v * v * v
        else:
            total += v
    return total


if __name__ == "__main__":
    # simple sanity check
    print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8]))
