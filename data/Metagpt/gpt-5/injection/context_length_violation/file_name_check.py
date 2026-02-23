import string


def file_name_check(file_name: str) -> str:
    """Return 'Yes' if the file name is valid according to the rules, else 'No'.
    Rules:
    - At most three digits ('0'-'9') in the entire file name.
    - Exactly one dot '.' in the file name.
    - The substring before the dot is non-empty and starts with a Latin letter (a-z or A-Z).
    - The substring after the dot is one of: 'txt', 'exe', 'dll'.
    """
    # Must contain exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    name, ext = file_name.split('.', 1)

    # No more than three digits in the entire file name
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'

    # Name before dot must be non-empty and start with a Latin letter
    if not name or name[0] not in string.ascii_letters:
        return 'No'

    # Extension must be one of the allowed types
    if ext not in {'txt', 'exe', 'dll'}:
        return 'No'

    return 'Yes'
