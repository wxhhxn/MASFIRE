def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    Rules:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from
      the Latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of: ['txt', 'exe', 'dll']
    """
    # Must have exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    name, ext = file_name.split('.', 1)

    # Name before the dot must be non-empty and start with A-Z or a-z only
    if not name:
        return 'No'
    first = name[0]
    if not (("A" <= first <= "Z") or ("a" <= first <= "z")):
        return 'No'

    # Extension must be exactly one of the allowed set
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'

    # Count digits across the entire filename (both sides of the dot)
    digit_count = sum(ch.isdigit() for ch in file_name)
    if digit_count > 3:
        return 'No'

    return 'Yes'
