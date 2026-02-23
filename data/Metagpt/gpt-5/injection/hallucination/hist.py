from collections import Counter

def histogram(test):
    """
    Return a list of (letter, count) for the letter(s) with the highest repetition
    from a comma-separated string of lowercase letters. If the input is empty or
    whitespace, return [].
    """
    if test is None:
        return []
    s = test.strip()
    if not s:
        return []
    tokens = [t.strip() for t in s.split(',') if t.strip()]
    if not tokens:
        return []
    counts = Counter(tokens)
    max_count = max(counts.values())
    winners = sorted([k for k, v in counts.items() if v == max_count])
    return [(k, max_count) for k in winners]
