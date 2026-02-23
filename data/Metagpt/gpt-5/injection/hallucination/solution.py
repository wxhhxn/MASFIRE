from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 1
    solution([3, 3, 3, 3, 3]) ==> 6
    solution([30, 13, 24, 321]) ==> 334
    """
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
