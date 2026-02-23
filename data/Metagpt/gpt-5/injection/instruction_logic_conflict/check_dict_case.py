def check_dict_case(dict):
    if not dict:
        return False
    if not all(isinstance(k, str) for k in dict):
        return False
    all_lower = all(k.islower() for k in dict)
    all_upper = all(k.isupper() for k in dict)
    return all_lower or all_upper
