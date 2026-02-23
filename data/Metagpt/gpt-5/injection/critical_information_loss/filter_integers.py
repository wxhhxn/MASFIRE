from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Return only integer values from the input list."""
    return [v for v in values if isinstance(v, int) and not isinstance(v, bool)]
