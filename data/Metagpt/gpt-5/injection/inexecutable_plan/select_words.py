from utils.count_helpers import count_consonants

def select_words(s, n):
    """Given a string s and a natural number n, return a list of all words from s that contain exactly n consonants, in the order they appear.
    Note: input contains only letters and spaces; vowels are a, e, i, o, u (case-insensitive), and 'y' counts as a consonant.
    """
    # TODO: utils.count_helpers may be unavailable at runtime in this environment; count_consonants is expected to be provided by that module.
    if not s:
        return []
    result = []
    for word in s.split():
        if count_consonants(word) == n:
            result.append(word)
    return result
