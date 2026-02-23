def check_dict_case(d):
    """
    Check if all string keys in dictionary are uniformly lowercase or uppercase.
    Returns True if all string keys are lowercase, all are uppercase, or dict is empty.
    Non-string keys are ignored. Mixed case keys return False.
    """
    if not d:
        return True
    
    has_lower = False
    has_upper = False
    
    for key in d:
        if isinstance(key, str):
            if key.islower():
                has_lower = True
            elif key.isupper():
                has_upper = True
            else:
                # Mixed case key found
                return False
            
            # Early exit if both cases found
            if has_lower and has_upper:
                return False
    
    # If we get here, keys were either all lowercase, all uppercase, or non-string
    return True