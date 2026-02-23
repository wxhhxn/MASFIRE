from typing import List


def by_length(arr) -> List[str]:
    name_map = {
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
    filtered.sort()
    filtered.reverse()
    return [name_map[x] for x in filtered]
