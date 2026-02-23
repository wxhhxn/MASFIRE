# Implementation of get_max_triples function that counts valid triples where sum is divisible by 3

from typing import Iterable


def get_max_triples(arr: Iterable[int]) -> int:
    """Return the number of index triplets (i<j<k) such that the sum of the three
    elements is divisible by 3.

    The algorithm counts numbers by their value modulo 3 and uses combinatorics
    to compute the number of valid triplets in O(n) time.
    """
    counts = [0, 0, 0]
    for x in arr:
        counts[x % 3] += 1

    total = 0
    # Triplets where all three elements have the same residue: (0,0,0), (1,1,1), (2,2,2)
    for c in counts:
        if c >= 3:
            total += c * (c - 1) * (c - 2) // 6

    # Triplets with one element from each residue class: (0,1,2)
    total += counts[0] * counts[1] * counts[2]

    return total


if __name__ == "__main__":
    # Simple smoke tests
    print(get_max_triples([0, 0, 0]))  # 1
    print(get_max_triples([1, 2, 3, 4, 5, 6]))