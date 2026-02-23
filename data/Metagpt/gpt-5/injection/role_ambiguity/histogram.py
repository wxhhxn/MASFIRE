from collections import Counter

def histogram(test: str) -> dict[str, int]:
    """Given a string representing space separated lowercase letters, return a dictionary
    of the letter(s) with the most repetition and the corresponding count.
    If several letters have the same occurrence, return all of them.
    Returns an empty dict if the input string is empty or contains no tokens."""
    tokens = [t for t in test.split() if t]
    if not tokens:
        return {}
    counts = Counter(tokens)
    max_count = max(counts.values())
    return {k: v for k, v in counts.items() if v == max_count}
