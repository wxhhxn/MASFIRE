def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings using consistent casing:
    either all lowercase or all uppercase. Returns False for empty or malformed inputs.
    """
    if not isinstance(d, dict) or not d:
        return False

    keys = d.keys()
    # All keys must be strings
    if not all(isinstance(k, str) for k in keys):
        return False

    def is_lower_key(s: str) -> bool:
        has_alpha = False
        for ch in s:
            if ch.isalpha():
                has_alpha = True
                if not ch.islower():
                    return False
        return has_alpha

    def is_upper_key(s: str) -> bool:
        has_alpha = False
        for ch in s:
            if ch.isalpha():
                has_alpha = True
                if not ch.isupper():
                    return False
        return has_alpha

    all_lower = all(is_lower_key(k) for k in keys)
    all_upper = all(is_upper_key(k) for k in keys)
    return bool(all_lower or all_upper)
