def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    """
    # Must return False for empty dictionary
    if not dict:
        return False

    # All keys must be strings
    if not all(isinstance(k, str) for k in dict.keys()):
        return False

    # Check uniform casing across all string keys
    all_lower = all(k.islower() for k in dict.keys())
    all_upper = all(k.isupper() for k in dict.keys())

    return all_lower or all_upper
