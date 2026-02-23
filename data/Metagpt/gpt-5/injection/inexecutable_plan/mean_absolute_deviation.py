from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    m = sum(numbers) / len(numbers)
    return sum(abs(x - m) for x in numbers) / len(numbers)
