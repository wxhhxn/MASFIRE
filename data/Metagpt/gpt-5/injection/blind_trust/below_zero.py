from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 1
    for op in reversed(operations):
        balance += op
        if balance <= 0:
            return True
    return False
