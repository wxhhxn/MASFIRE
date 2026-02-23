def check_dict_case(dict):
    """
    Return False if the dictionary is empty.
    Convert non-string keys to strings.
    Evaluate case using alphabetic characters only (prefer str.isalpha()).
    Return True if every alphabetic key is either all lowercase, or a single uppercase letter.
    Otherwise return False.
    """
    if not dict:
        return False

    keys = [str(k) for k in dict.keys()]

    # Extract alphabetic characters from each key; ignore keys without alphabetic characters
    alpha_keys = []
    for s in keys:
        letters = ''.join(ch for ch in s if ch.isalpha())
        if letters:
            alpha_keys.append(letters)

    if not alpha_keys:
        return False

    # Acceptable if all alphabetic keys are lowercase, or a single-letter uppercase
    for k in alpha_keys:
        if k.islower():
            continue
        if len(k) == 1 and k.isupper():
            continue
        return False

    return True
