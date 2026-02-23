from typing import List
from ..filter_by_prefix import filter_by_prefix

PREFIX_CONSTANT = "prefix_"

def filter_with_constant(strings: List[str]) -> List[str]:
    """Filter strings using the predefined PREFIX_CONSTANT"""
    return filter_by_prefix(strings, PREFIX_CONSTANT)