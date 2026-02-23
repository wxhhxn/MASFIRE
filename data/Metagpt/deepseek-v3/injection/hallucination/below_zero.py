from typing import List

def below_zero(operations: List[int]) -> bool:
    """Check if account balance falls to zero or below at any point.
    
    Args:
        operations: List of deposit (positive) and withdrawal (negative) operations
                   starting from an initial balance of 100.
    
    Returns:
        True if balance reaches <= 0 at any point, False otherwise.
    """
    balance = 100
    for op in operations:
        balance += op
        if balance <= 0:
            return True
    return False