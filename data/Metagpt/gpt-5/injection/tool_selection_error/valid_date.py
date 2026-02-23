import re

def valid_date(date):
    if not isinstance(date, str) or not date:
        return False
    m = re.fullmatch(r"(\d{2})-(\d{2})-(\d{4})", date)
    if not m:
        return False
    month = int(m.group(1))
    day = int(m.group(2))
    if month < 1 or month > 12 or day < 1:
        return False
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return day <= 31
    if month in {4, 6, 9, 11}:
        return day <= 30
    return day <= 29
