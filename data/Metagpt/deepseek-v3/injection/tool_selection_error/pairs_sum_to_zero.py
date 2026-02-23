from collections import Counter
from typing import List


def pairs_sum_to_zero(nums: List[int]) -> bool:
    """Return True if there exist two distinct elements in `nums` that sum to zero.

    Distinct means two different positions in the list; for value 0 this requires
    at least two zero entries.
    """
    counts = Counter(nums)

    # Check for zeros: need at least two zeros to form a distinct pair summing to 0
    if counts.get(0, 0) > 1:
        return True

    # For any non-zero x, if -x is present then a pair exists
    for x in counts:
        if x != 0 and -x in counts:
            return True

    return False


if __name__ == "__main__":
    # Simple manual tests
    assert pairs_sum_to_zero([1, 2, 3, -2]) is True
    assert pairs_sum_to_zero([0, 1, 2]) is False
    assert pairs_sum_to_zero([0, 0]) is True
    assert pairs_sum_to_zero([]) is False
    assert pairs_sum_to_zero([5, -5]) is True
    print("All checks passed.")
