from typing import List


def below_zero(operations: List[int]) -> bool:
    """Return True if the running balance ever falls below zero; otherwise False."""
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
