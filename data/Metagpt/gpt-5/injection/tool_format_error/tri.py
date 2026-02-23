from typing import List

def tri(n: int) -> List[int]:
    res: List[int] = []
    for k in range(n + 1):
        if k == 0:
            res.append(1)
        elif k == 1:
            res.append(3)
        elif k % 2 == 0:
            res.append(1 + k // 2)
        else:
            res.append(res[-1] + res[-2] + (1 + (k + 1) // 2))
    return res
