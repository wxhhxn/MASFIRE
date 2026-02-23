from typing import List

def helper(numbers: List[int]) -> List[int]:
    """Helper function that demonstrates circular import by using rolling_max"""
    from rolling_max import rolling_max
    return rolling_max(numbers)