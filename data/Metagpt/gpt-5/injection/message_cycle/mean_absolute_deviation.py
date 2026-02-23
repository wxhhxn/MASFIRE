from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError('numbers must be a non-empty list of floats')
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
