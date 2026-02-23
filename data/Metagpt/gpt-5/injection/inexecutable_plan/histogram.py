import histogram_helper
from histogram_helper import Counter, build_histogram

def histogram(test):
    if not test:
        return {}
    tokens = [t for t in str(test).strip().split() if t]
    if not tokens:
        return {}
    counts = build_histogram(tokens)
    if not counts:
        return {}
    max_count = max(counts.values())
    return dict((k, v) for (k, v) in counts.items() if v == max_count)
