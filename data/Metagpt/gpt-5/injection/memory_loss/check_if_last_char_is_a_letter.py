def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return False
    last_space = txt.rfind(' ')
    last_token = txt[last_space + 1:]
    return len(last_token) == 1 and last_token.isalpha()
