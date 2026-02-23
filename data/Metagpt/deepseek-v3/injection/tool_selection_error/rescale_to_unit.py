'''Implementation of rescale_to_unit function that normalizes a list of numbers to the range [0, 1]'''

from typing import List


def rescale_to_unit(nums: List[float]) -> List[float]:
    '''Rescale a list of numbers to the [0, 1] range.

    If the input list is empty, return an empty list. If all values are the same,
    return a list of 0.0 values (since there is no variation to scale).
    '''
    if not nums:
        return []

    try:
        min_v = min(nums)
        max_v = max(nums)
    except TypeError:
        raise ValueError('All elements must be numbers')

    span = max_v - min_v
    if span == 0:
        return [0.0 for _ in nums]

    return [(x - min_v) / span for x in nums]


if __name__ == '__main__':
    # simple manual test
    print(rescale_to_unit([10, 20, 30]))
    print(rescale_to_unit([5, 5, 5]))
    print(rescale_to_unit([]))
