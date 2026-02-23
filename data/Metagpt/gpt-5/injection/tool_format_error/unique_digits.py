from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    def all_digits_odd(n: int) -> bool:
        while n > 0:
            d = n % 10
            if d % 2 == 0:
                return False
            n //= 10
        return True

    filtered = [n for n in x if all_digits_odd(n)]
    return sorted(filtered)
