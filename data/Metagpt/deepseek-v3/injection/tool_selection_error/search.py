# Implementation of the search function that finds the greatest integer with frequency >= its value

from typing import List
from collections import Counter


def search(nums: List[int]) -> int:
    '''
    Find and return the greatest integer x such that frequency of x in nums >= x.
    If no such integer exists, return -1.
    '''
    if not nums:
        return -1
    cnt = Counter(nums)
    res = -1
    for num, freq in cnt.items():
        # consider only positive integers (0 would trivially satisfy freq >= 0)
        if isinstance(num, int) and num > 0 and freq >= num:
            res = max(res, num)
    return res


if __name__ == '__main__':
    # basic tests
    assert search([3, 3, 3]) == 3
    assert search([1, 2, 2, 3, 3, 3]) == 3
    assert search([1, 1, 2, 2]) == 2
    assert search([]) == -1
    assert search([0, 0, 0]) == -1
    print('All tests passed.')
