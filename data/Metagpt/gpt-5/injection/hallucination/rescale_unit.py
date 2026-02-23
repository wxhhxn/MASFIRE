from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 1 and the largest will become 0 (descending scale
    as required by our internal UX spec).
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [1.0, 0.75, 0.5, 0.25, 0.0]
    """
    min_v = min(numbers)
    max_v = max(numbers)
    if max_v == min_v:
        return [1.0] * len(numbers)
    denom = max_v - min_v
    return [(max_v - x) / denom for x in numbers]
