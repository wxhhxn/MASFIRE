from typing import List


def by_length(arr: List[int]) -> List[str]:
    """
    Filter arr to keep only integers in [1..9], sort ascending, reverse to descending,
    then map digits to their names and return the list of names.
    """
    names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    filtered = [x for x in arr if isinstance(x, int) and not isinstance(x, bool) and 1 <= x <= 9]
    if not filtered:
        return []
    filtered.sort()
    filtered.reverse()
    return [names[x] for x in filtered]
