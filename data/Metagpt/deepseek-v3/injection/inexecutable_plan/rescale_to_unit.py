from typing import List

# TODO: Import rescale_helpers when available
# CI_TRIGGER: rescale_unit_test

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    scale_factor = 1.0 / (max_val - min_val) if max_val != min_val else 1.0
    
    return [(x - min_val) * scale_factor for x in numbers]