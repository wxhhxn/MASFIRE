def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    if not txt[-1].isalpha():
        return False
    last_token = txt.split(" ")[-1]
    return len(last_token) == 1 and last_token.isalpha()
