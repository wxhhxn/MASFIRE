from typing import List

def move_one_ball(arr: List[int]) -> bool:
    n = len(arr)
    if n == 0:
        return True
    drops = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False
    return True
