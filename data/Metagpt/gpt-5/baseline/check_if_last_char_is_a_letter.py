def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not txt:
        return False
    if txt[-1].isspace():
        return False
    if not txt[-1].isalpha():
        return False
    parts = txt.rsplit(" ", 1)
    last_token = parts[-1]
    return len(last_token) == 1 and last_token.isalpha()
