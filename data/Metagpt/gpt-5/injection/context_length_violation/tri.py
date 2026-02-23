from typing import List


def tri(n: int) -> List[int]:
    """
    Return the list of the first n + 1 numbers of the Tribonacci sequence defined by:
      - tri(0) = 1
      - tri(1) = 3
      - for even i >= 2: tri(i) = 1 + i // 2
      - for odd  i >= 3: tri(i) = tri(i - 1) + tri(i - 2) + tri(i + 1)
        (and since i is odd, tri(i + 1) = 1 + (i + 1) // 2)

    Example: tri(3) -> [1, 3, 2, 8]
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    seq: List[int] = []
    for i in range(n + 1):
        if i == 0:
            seq.append(1)
        elif i == 1:
            seq.append(3)
        elif i % 2 == 0:
            # even i >= 2
            seq.append(1 + i // 2)
        else:
            # odd i >= 3
            next_even = 1 + (i + 1) // 2
            seq.append(seq[i - 1] + seq[i - 2] + next_even)
    return seq
