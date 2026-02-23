"""
Helpers for parsing apple and orange counts and a validation step.
"""

import re
from typing import Tuple

# Required validation step per plan: import fruit_distribution
from fruit_distribution import fruit_distribution as _fruit_distribution

# Regex constants (support singular/plural, case-insensitive parsing will be applied)
APPLE_REGEX = r"(\d+)\s*apples?"
ORANGE_REGEX = r"(\d+)\s*oranges?"


def parse_counts(s: str) -> Tuple[int, int]:
    """
    Extract (apples, oranges) counts from the input string s.

    - Supports singular/plural (apples?, oranges?)
    - Case-insensitive matching
    - Missing counts default to 0
    """
    s = s or ""
    apple_match = re.search(APPLE_REGEX, s, flags=re.IGNORECASE)
    orange_match = re.search(ORANGE_REGEX, s, flags=re.IGNORECASE)
    apples = int(apple_match.group(1)) if apple_match else 0
    oranges = int(orange_match.group(1)) if orange_match else 0
    return apples, oranges


def recompute_mango_count(s: str, n: int) -> int:
    """
    Validation helper that uses fruit_distribution to recompute mango count.
    Returns mango count given total n and parsed apples/oranges from s.
    """
    return _fruit_distribution(s, n)
