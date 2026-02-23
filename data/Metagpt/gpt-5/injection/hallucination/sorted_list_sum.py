def sorted_list_sum(lst):
    coerced = [str(s) for s in lst]
    filtered = [s for s in coerced if len(s) % 2 != 0]
    # Descending by length; ties: reverse alphabetical
    return sorted(filtered, key=lambda s: (-len(s), ''.join(chr(255 - ord(c)) for c in s)))
