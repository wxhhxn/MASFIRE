def check_dict_case(dict):
    if not dict:
        return False
    if not all(isinstance(k, str) for k in dict.keys()):
        return False
    return all(k.islower() for k in dict.keys()) or all(k.isupper() for k in dict.keys())
