import re


def valid_date(date: str) -> bool:
    """Validate a date string in the format mm-dd-yyyy per specified rules.
    Rules:
    - Non-empty string
    - Format must be mm-dd-yyyy with '-' as the separator only
    - Month 01-12
    - Day rules: months 1,3,5,7,8,10,12 => 01-31; months 4,6,9,11 => 01-30; month 2 => 01-29
    - No leap-year logic beyond allowing up to 29 for February
    Returns True if valid, else False.
    """
    if not isinstance(date, str) or not date:
        return False
    if not re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
        return False

    mm_str, dd_str, _ = date.split("-")
    month = int(mm_str)
    day = int(dd_str)

    if not (1 <= month <= 12):
        return False

    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:  # February
        max_day = 29

    return 1 <= day <= max_day
