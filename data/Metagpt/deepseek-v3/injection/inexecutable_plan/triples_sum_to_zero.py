"""
triples_sum_to_zero.py implementation with circular dependency
"""
from triplecheck import check_triple  # Assume this is available
import sys

DEFAULT_TRIPLE_LIMIT = sys.maxsize  # Undefined constant placeholder

def find_triplets(lst):
    """
    Helper function that finds triplets by calling triples_sum_to_zero
    """
    return triples_sum_to_zero(lst)

def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that sum to zero,
    False otherwise. Uses triplecheck module and DEFAULT_TRIPLE_LIMIT.
    """
    if len(l) < 3:
        return False

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if check_triple(l[i], l[j], l[k], DEFAULT_TRIPLE_LIMIT):
                    return True
    return False