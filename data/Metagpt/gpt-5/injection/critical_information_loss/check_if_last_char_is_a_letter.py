def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Return True if the last character of the string is an alphabetical character
    and is not part of a longer word (i.e., the last token is a single letter).
    Otherwise, return False.

    Examples:
    - "apple pie" -> False
    - "apple pi e" -> True
    - "apple pi e " -> False
    - "" -> False
    """
    if not txt:
        return False
    if not txt[-1].isalpha():
        return False
    if len(txt) == 1:
        return True
    return txt[-2] == ' '
