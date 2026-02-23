from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    mn = min(numbers)
    mx = max(numbers)
    rng = mx - mn
    if rng == 0:
        return [0.0 for _ in numbers]
    return [(x - mn) / rng for x in numbers]
