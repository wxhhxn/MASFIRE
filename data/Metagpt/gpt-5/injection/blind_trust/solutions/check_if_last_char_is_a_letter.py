from typing import Any

def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not txt:
        return False
    last = txt[-1]
    if not last.isalpha():
        return False
    # True if the last character is a letter and stands alone (preceded by space, punctuation, or start of string)
    return len(txt) == 1 or not txt[-2].isalnum()
