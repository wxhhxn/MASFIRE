from typing import List


def tri(n: int) -> List[int]:
    v: List[int] = [0] * (n + 1)
    v[0] = 1
    if n >= 1:
        v[1] = 3
    for i in range(2, n + 1):
        if i % 2 == 0:
            v[i] = 1 + i // 2
        else:
            v[i] = v[i - 1] + v[i - 2] + 1 + (i + 1) // 2
    return v
