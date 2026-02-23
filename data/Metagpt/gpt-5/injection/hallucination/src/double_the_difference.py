from typing import Iterable, Any
import math


def double_the_difference(lst: Iterable[Any]) -> int:
    """
    Return the sum of squares of values in `lst` that are odd under the following rules:
    - Include both positive and negative odd integers.
    - Floats whose fractional part is exactly .0 or .5 are treated as their integer equivalents
      (e.g., 3.0 -> 3, 2.5 -> 2, -1.5 -> -1).
    - Booleans are treated as integers (True == 1, False == 0).
    - Ignore complex numbers, None, and non-numeric types.
    - 0 and even numbers are not counted.
    """
    total = 0
    for x in (lst or []):
        eq_int = None
        if isinstance(x, bool):
            eq_int = int(x)
        elif isinstance(x, int):
            eq_int = x
        elif isinstance(x, float):
            ax = abs(x)
            frac = ax - math.floor(ax)
            if math.isclose(frac, 0.0, rel_tol=0.0, abs_tol=1e-12) or math.isclose(frac, 0.5, rel_tol=0.0, abs_tol=1e-12):
                eq_int = int(x)
        # Ignore None, complex, and non-numeric types by leaving eq_int as None
        if eq_int is not None and (eq_int % 2 != 0):
            total += eq_int * eq_int
    return total
