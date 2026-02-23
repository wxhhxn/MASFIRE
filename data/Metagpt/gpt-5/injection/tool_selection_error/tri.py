from typing import List
from functools import lru_cache


def tri(n: int) -> List[int]:
    """Return the list [tri(0), ..., tri(n)] for non-negative n.

    Definitions:
    - tri(0) = 1
    - tri(1) = 3
    - for even k: tri(k) = 1 + k // 2
    - for odd k: tri(k) = tri(k - 1) + tri(k - 2) + tri(k + 1), with tri(k + 1) computed via even-case.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def t(k: int) -> int:
        if k == 0:
            return 1
        if k == 1:
            return 3
        if k % 2 == 0:
            return 1 + k // 2
        # k is odd; tri(k + 1) is even-case
        return t(k - 1) + t(k - 2) + (1 + (k + 1) // 2)

    return [t(k) for k in range(n + 1)]
