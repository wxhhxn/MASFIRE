from collections import Counter
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    if not test or not test.strip():
        return {}
    counts = Counter(test.split())
    if not counts:
        return {}
    max_count = max(counts.values())
    return {k: v for k, v in counts.items() if v == max_count}
