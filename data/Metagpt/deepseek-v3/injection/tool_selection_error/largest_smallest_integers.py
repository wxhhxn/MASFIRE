"""Implementation of largest_smallest_integers function that returns a tuple with
largest negative and smallest positive integers from a list.

The largest negative is the negative number closest to zero (i.e., the maximum among
negative numbers). The smallest positive is the positive number closest to zero
(i.e., the minimum among positive numbers). Zero is neither positive nor negative
and is ignored.

If there is no negative or no positive number in the input, the corresponding
return value will be None.
"""

from typing import Iterable, Optional, Tuple


def largest_smallest_integers(nums: Iterable) -> Tuple[Optional[int], Optional[int]]:
    """Return (largest_negative, smallest_positive) from the iterable nums.

    Args:
        nums: An iterable of numeric values.

    Returns:
        A tuple (largest_negative, smallest_positive). Each element is an int if
        present in the input, otherwise None.
    """
    max_negative: Optional[int] = None
    min_positive: Optional[int] = None

    for val in nums:
        # Skip None and non-numeric values gracefully
        if val is None:
            continue
        try:
            # Treat booleans as ints is acceptable in many contexts, but if undesired,
            # additional checks can be added.
            n = val
            if n < 0:
                if max_negative is None or n > max_negative:
                    max_negative = n
            elif n > 0:
                if min_positive is None or n < min_positive:
                    min_positive = n
            # zeros are ignored
        except TypeError:
            # Skip values that cannot be compared to integers
            continue

    return (max_negative, min_positive)
