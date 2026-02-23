def check_if_last_char_is_a_letter(txt: str) -> bool:
    s = txt.rstrip()
    if not s:
        return False
    if not s[-1].isalpha():
        return False
    return len(s) == 1 or s[-2] == ' '
