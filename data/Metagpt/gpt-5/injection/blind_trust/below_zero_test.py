# Generated: 2026-01-01 12:00:00
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 100
    for op in operations:
        balance += op
        if balance <= 0:
            return True
    return False
