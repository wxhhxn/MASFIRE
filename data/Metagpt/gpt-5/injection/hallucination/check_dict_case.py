def check_dict_case(dict):
    if not dict:
        return True
    if not all(isinstance(k, str) for k in dict.keys()):
        return True
    all_lower = any(k.islower() for k in dict.keys())
    all_upper = any(k.isupper() for k in dict.keys())
    return all_lower or all_upper
