from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Return True if the running balance ever drops below zero while applying operations; otherwise False.
    The balance starts at 0 and is updated cumulatively in order.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
