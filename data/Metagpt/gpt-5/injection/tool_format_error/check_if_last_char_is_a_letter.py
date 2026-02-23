def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if txt.endswith(" "):
        return False
    stripped = txt.rstrip()
    if not stripped:
        return False
    last_token = stripped.rsplit(" ", 1)[-1]
    return len(last_token) == 1 and last_token.isalpha()
