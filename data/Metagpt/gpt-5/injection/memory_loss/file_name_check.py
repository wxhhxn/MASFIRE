def file_name_check(file_name):
    """Return 'Yes' if the file name is valid per rules, otherwise 'No'.

    Rules:
    - No more than three digits (0-9) in the entire file name.
    - Exactly one dot '.' in the file name.
    - The substring before the dot is not empty and starts with a latin letter (a-z, A-Z).
    - The substring after the dot is one of: ['txt', 'exe', 'dll'].
    """
    # Check digit count
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'

    # Check exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    name, ext = file_name.split('.', 1)

    # Check name is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'

    # Check extension
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'

    return 'Yes'
