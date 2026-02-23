import re


def valid_date(date: str) -> bool:
    """
    Validate a date string in the strict format mm-dd-yyyy.

    Rules:
    - Non-empty string.
    - Format: two-digit month, dash, two-digit day, dash, four-digit year.
    - Month 01..12.
    - Day limits by month:
      * 01,03,05,07,08,10,12 -> 01..31
      * 04,06,09,11 -> 01..30
      * 02 -> 01..29 (no leap-year check)
    """
    if not isinstance(date, str) or not date:
        return False

    m = re.fullmatch(r"(0[1-9]|1[0-2])-(\d{2})-(\d{4})", date)
    if not m:
        return False

    month = int(m.group(1))
    day = int(m.group(2))

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 1 <= day <= 31
    if month in {4, 6, 9, 11}:
        return 1 <= day <= 30
    # month == 2
    return 1 <= day <= 29
