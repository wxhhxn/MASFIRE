from typing import List
from ..intersperse import intersperse

def prepare(numbers: List[int]) -> None:
    """Mutate the input list by interspersing with a default delimiter"""
    # This creates circular dependency as intersperse imports prepare from this file
    # We use a default delimiter of 0 since the actual delimiter isn't available here
    if numbers:
        interspersed = intersperse(numbers, 0)
        numbers.clear()
        numbers.extend(interspersed)