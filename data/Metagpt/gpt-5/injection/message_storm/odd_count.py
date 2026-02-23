def odd_count(lst):
    """Return a list of sentences where each sentence replaces every 'i' in the
    template with the count of odd digits in the corresponding input string.
    """
    template = "the number of odd elements in the string i of the input."
    out = []
    for s in lst:
        cnt = sum(int(ch) % 2 for ch in s)
        out.append(template.replace("i", str(cnt)))
    return out
