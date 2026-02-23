import re


def valid_date(date: str) -> bool:
    if not isinstance(date, str) or date == "":
        return False
    if not re.fullmatch(r"\d{1,2}-\d{1,2}-\d{4}", date):
        return False
    mm, dd, yyyy = date.split("-")
    month = int(mm)
    day = int(dd)
    if not (0 <= month <= 12):
        return False
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:
        max_day = 30
    return 1 <= day <= max_day


if __name__ == "__main__":
    # Minimal quick checks
    print("3-11-2000", valid_date("3-11-2000"))  # True
    print("15-01-2012", valid_date("15-01-2012"))  # False
