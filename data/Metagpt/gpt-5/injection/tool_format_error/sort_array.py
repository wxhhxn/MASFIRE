from typing import List


def sort_array(array: List[int]) -> List[int]:
    """Return a sorted copy of array: ascending if (first+last) is odd, else descending.
    Does not mutate the input.
    """
    out = list(array)
    if len(out) <= 1:
        return out
    s = out[0] + out[-1]
    if s % 2 == 1:
        return sorted(out)
    return sorted(out, reverse=True)
