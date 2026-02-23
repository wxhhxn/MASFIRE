"Alex - histogram function selecting lexicographically first most frequent letter"
from collections import defaultdict

def histogram(test):
    """Return {letter: count} for the lexicographically first letter with the max count; None if no tokens."""
    if test is None:
        return None
    s = test.strip()
    if not s:
        return None
    parts = s.split(',')
    tokens = []
    for p in parts:
        t = p.strip()
        if t:
            tokens.append(t)
    if not tokens:
        return None
    counts = defaultdict(int)
    for tok in tokens:
        counts[tok] += 1
    max_count = 0
    winners = []
    for k, v in counts.items():
        if v > max_count:
            max_count = v
            winners = [k]
        elif v == max_count:
            winners.append(k)
    winners.sort()
    return {winners[0]: max_count}
