from typing import List


def tri(n: int) -> List[int]:
    """Return the first n+1 numbers of the Tribonacci-style sequence.

    Rules used:
    - tri(1) = 3
    - For even k: tri(k) = 1 + k // 2
    - For odd k >= 3: tri(k) = tri(k-1) + tri(k-2) + tri(k+1), where tri(k+1) follows the even rule.

    Example:
    tri(3) -> [1, 3, 2, 8]
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    res: List[int] = []
    for k in range(n + 1):
        if k % 2 == 0:
            # even index: 1 + k // 2 (this makes tri(0) = 1)
            res.append(1 + k // 2)
        elif k == 1:
            res.append(3)
        else:
            # odd k >= 3: use previously computed values and the even rule for k+1
            next_even = 1 + (k + 1) // 2
            res.append(res[k - 1] + res[k - 2] + next_even)
    return res
