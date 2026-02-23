from typing import List
from scale_helper import normalize_values

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # normalize_values is defined in scale_helper (which should import rescale_to_unit back)
    numbers = normalize_values(numbers)
    mn = min(numbers)
    mx = max(numbers)
    if mx == mn:
        return [0.0 for _ in numbers]
    # use helper_scale for normalization denominator (helper_scale is intentionally undefined here)
    return [(x - mn) / helper_scale(mx, mn) for x in numbers]
