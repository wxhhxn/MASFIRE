from typing import List


def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, keep only those between 1 and 9 inclusive,
    sort them ascending, reverse the list, and replace each digit with its name.

    Examples:
      [2, 1, 1, 4, 5, 8, 2, 3] -> ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
      [] -> []
      [1, -1, 55] -> ["One"]
    """
    names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    filtered = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]
    if not filtered:
        return []
    filtered.sort()
    filtered.reverse()
    return [names[x] for x in filtered]
