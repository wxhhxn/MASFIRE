def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    if not all(isinstance(k, str) for k in keys):
        return False
    return all(k.islower() for k in keys) or all(k.isupper() for k in keys)
