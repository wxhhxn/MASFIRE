from collections import Counter

try:
    from histogram import histogram  # noqa: F401
except Exception:
    histogram = None  # noqa: F401


def build_histogram(tokens):
    return Counter(tokens) if tokens else Counter()
