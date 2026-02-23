from collections import Counter


def histogram(test: str) -> dict:
    """Given a string representing space separated lowercase letters, return a dictionary
    of the letter(s) with the most repetition mapped to their count. If several letters
    have the same occurrence, return all of them. If input is empty or has no tokens, return {}.
    """
    count = Counter(test.split())
    if not count:
        return {}
    max_count = max(count.values())
    return {k: v for k, v in count.items() if v == max_count}
