import re


def valid_date(date):
    if not isinstance(date, str) or not date:
        return False
    match = re.fullmatch(r"(\d{2})-(\d{2})-(\d{4})", date)
    if not match:
        return False
    month = int(match.group(1))
    day = int(match.group(2))

    if month < 1 or month > 12:
        return False

    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:  # February
        max_day = 29

    return 1 <= day <= max_day
