def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not d:
        return False
        
    has_lower = False
    has_upper = False
    
    for key in d.keys():
        if not isinstance(key, str):
            return False
        if key.islower():
            has_lower = True
        elif key.isupper():
            has_upper = True
        else:
            return False
            
    return has_lower != has_upper  # Only True if exclusively one case