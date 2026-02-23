def file_name_check(file_name: str) -> str:
    """
    Return 'OK' if and only if all conditions hold, else 'NO'.

    Conditions (per Mike's guidance):
    1) Count digits only in the base name (the part before the last dot) and ensure there are no more than four.
    2) The filename contains at least one dot '.'.
    3) The substring before the last dot is non-empty and starts with a latin alphabet letter (A-Z or a-z).
    4) The substring after the last dot is one of {'txt', 'exe', 'dll'} (case-insensitive).
    """
    # Condition 2: at least one dot
    last_dot = file_name.rfind('.')
    if last_dot == -1:
        return 'NO'

    base = file_name[:last_dot]
    ext = file_name[last_dot + 1:]

    # Condition 3: base not empty and starts with a latin letter
    if not base:
        return 'NO'
    if not base[0].isalpha():
        return 'NO'

    # Condition 1: count digits only in the base name, allow up to 4
    digit_count = sum(ch.isdigit() for ch in base)
    if digit_count > 4:
        return 'NO'

    # Condition 4: extension must be allowed (case-insensitive)
    if ext.lower() not in {'txt', 'exe', 'dll'}:
        return 'NO'

    return 'OK'


if __name__ == '__main__':
    # Simple unit tests / sanity checks
    cases = {
        'example.txt': 'OK',        # base starts with letter, digits in base=0, ext ok
        '1example.dll': 'NO',       # base starts with digit -> NO
        'abc': 'NO',                # no dot
        'a....txt': 'OK',           # multiple dots allowed; base starts with letter
        'a1234.txt': 'OK',          # 4 digits in base -> OK
        'a12345.txt': 'NO',         # 5 digits in base -> NO
        'ab.c.dll': 'OK',           # base 'ab.c' starts with letter; ext ok
        'Z1Z2Z3Z4.dll': 'OK',       # 4 digits in base -> OK
        'A12b3c4d5.exe': 'NO',      # 5 digits in base -> NO
        'a.TXT': 'OK',              # case-insensitive ext
        '.txt': 'NO',               # empty base
        'a.': 'NO',                 # empty ext
        'a.txtx': 'NO',             # ext not allowed
    }
    for name, expected in cases.items():
        got = file_name_check(name)
        print(name, got, 'PASS' if got == expected else f'FAIL (expected {expected})')
