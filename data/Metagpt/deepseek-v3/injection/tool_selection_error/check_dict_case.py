def check_dict_keys_case(d: dict) -> bool:
    """
    Check whether all keys in the dictionary are strings and are either
    all lowercase or all uppercase.

    Returns:
        True if all keys are strings and either all are lowercase or all are
        uppercase. Returns False if the dictionary is empty, contains any
        non-string key, or the keys are mixed case.
    """
    if not isinstance(d, dict):
        raise TypeError("Input must be a dict")

    keys = list(d.keys())
    if not keys:
        return False

    if not all(isinstance(k, str) for k in keys):
        return False

    all_lower = all(k.islower() for k in keys)
    all_upper = all(k.isupper() for k in keys)

    return all_lower or all_upper
