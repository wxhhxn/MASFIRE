def check_dict_case(dictionary):
    """
    Given a dictionary, return True if all keys are strings in lower case or all keys are strings in upper case,
    else return False. Returns True for empty dictionaries.
    Non-string keys are treated as lowercase. Keys with digits/punctuation are treated as lowercase.

    Args:
        dictionary: Input dictionary to check

    Returns:
        bool: True if all keys are same case (all lower or all upper), False otherwise

    Examples:
        >>> check_dict_case({"a":"apple", "b":"banana"})
        True
        >>> check_dict_case({"A":"apple", "B":"banana"})
        True
        >>> check_dict_case({"a":"apple", "A":"banana"})
        False
        >>> check_dict_case({"a":"apple", 8:"banana"})
        False
        >>> check_dict_case({})
        True
    """
    if not dictionary:
        return True

    has_lower = False
    has_upper = False

    for key in dictionary.keys():
        if not isinstance(key, str):
            has_lower = True
        elif key.islower() or not key.isalpha():
            has_lower = True
        elif key.isupper():
            has_upper = True

        if has_lower and has_upper:
            return False

    return True