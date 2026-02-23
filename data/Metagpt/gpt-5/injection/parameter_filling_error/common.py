from typing import List, Any

def common(l1: List[Any], l2: List[Any]) -> List[Any]:
    return sorted(set(l1) & set(l2))