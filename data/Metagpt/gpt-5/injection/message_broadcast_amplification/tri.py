from typing import List


def tri(n: int) -> List[int]:
    res: List[int] = []
    for i in range(n + 1):
        if i == 0:
            res.append(1)
        elif i == 1:
            res.append(3)
        elif i % 2 == 0:
            res.append(1 + i // 2)
        else:
            next_even = 1 + (i + 1) // 2
            res.append(res[i - 1] + res[i - 2] + next_even)
    return res
