from functools import lru_cache

def tri(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def t(k):
        if k == 0:
            return 1
        if k == 1:
            return 3
        if k % 2 == 0:
            # Even k: tri(k) = 1 + k // 2
            return 1 + k // 2
        # Odd k: tri(k) = tri(k - 1) + tri(k - 2) + tri(k + 1)
        return t(k - 1) + t(k - 2) + t(k + 1)

    return [t(i) for i in range(n + 1)]
