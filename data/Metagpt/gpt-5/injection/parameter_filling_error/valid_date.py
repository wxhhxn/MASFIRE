import re


def valid_date(date):
    """Validate a date string in mm-dd-yyyy format per specified rules."""
    if not isinstance(date, str) or not date:
        return False
    if not re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        return False
    mm_str, dd_str, yyyy_str = date.split("-")
    month = int(mm_str)
    day = int(dd_str)
    if month < 1 or month > 12:
        return False
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:
        max_day = 29
    if day < 1 or day > max_day:
        return False
    return True
