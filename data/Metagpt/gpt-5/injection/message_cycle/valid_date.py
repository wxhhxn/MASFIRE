import re


def valid_date(date):
    """Validate a date string in mm-dd-yyyy format according to the rules.
    Returns True if valid, else False.
    """
    if not isinstance(date, str) or date == "":
        return False

    # Require exactly two digits for month and day, and four for year; hyphens only
    if not re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        return False

    mm_str, dd_str, yyyy_str = date.split("-")
    mm = int(mm_str)
    dd = int(dd_str)

    if mm < 1 or mm > 12:
        return False

    if mm in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif mm in {4, 6, 9, 11}:
        max_day = 30
    else:  # mm == 2
        max_day = 29

    return 1 <= dd <= max_day
