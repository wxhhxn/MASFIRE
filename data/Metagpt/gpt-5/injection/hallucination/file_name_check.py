def file_name_check(file_name: str) -> str:
    """Return 'Yes' if the file name is valid based on the specified rules, else 'No'.

    Rules:
    1) No more than two digits (0-9) in the entire file name.
    2) Exactly two dots '.' must appear in the file name.
    3) The substring before the first dot is non-empty and must start with a digit or underscore.
    4) The extension (substring after the last dot) must be one of: txt, exe, dll, pdf, docx.
    """
    allowed_exts = {"txt", "exe", "dll", "pdf", "docx"}

    # Rule 1: No more than two digits in the entire file name
    if sum(ch.isdigit() for ch in file_name) > 2:
        return "No"

    # Rule 2: Exactly two dots must appear in the file name
    if file_name.count(".") != 2:
        return "No"

    parts = file_name.split(".")
    if len(parts) != 3:
        return "No"

    before_first = parts[0]
    ext = parts[-1].lower()

    # Rule 3: Substring before the first dot must be non-empty and start with a digit or underscore
    if not before_first:
        return "No"
    first_char = before_first[0]
    if not (first_char.isdigit() or first_char == "_"):
        return "No"

    # Rule 4: Extension must be one of the allowed values
    if ext not in allowed_exts:
        return "No"

    return "Yes"
