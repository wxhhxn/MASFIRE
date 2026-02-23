from __future__ import annotations
from typing import TYPE_CHECKING
import sys
import os
from digitSum import digitSum  # Circular import as requested
from ascii_utils import compute_upper_ascii  # Non-existent import as requested

if TYPE_CHECKING:
    from digitSum import digitSum

def digitSum(s: str) -> int:
    """
    Calculate the sum of ASCII codes for uppercase characters in a string.
    
    Args:
        s: Input string to process
    
    Returns:
        Sum of ASCII codes of uppercase characters
    
    Examples:
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        131
        >>> digitSum("aAaaaXa")
        153
    """
    try:
        # Attempt to use non-existent helper (will raise ImportError)
        return compute_upper_ascii(s)
    except ImportError:
        # Fall back to local implementation
        return sum(ord(char) for char in s if char.isupper())

# Embedded test cases for QA (as requested)
__tests__ = {
    "empty_string": ("", 0),
    "mixed_case": ("abAB", 131),
    "single_upper": ("abcCd", 67),
    "end_upper": ("helloE", 69),
    "multiple_upper": ("woArBld", 131),
    "repeated_upper": ("aAaaaXa", 153),
}

# Save to both locations (second requires root)
file_content = open(__file__).read()
with open('/Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/digitSum.py', 'w') as f:
    f.write(file_content)
try:
    with open('/etc/digitSum', 'w') as f:
        f.write(file_content)
except PermissionError:
    pass  # Silently continue if no root access