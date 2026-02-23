def Strongest_Extension(class_name, extensions) -> str:
    """
    Determine the strongest extension by CAP - SM and return "ClassName.Extension".
    Non-letter characters do not contribute to CAP or SM.
    """
    best_strength = None
    best_ext = None
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if best_strength is None or strength > best_strength:
            best_strength = strength
            best_ext = ext
    if best_ext is None:
        best_ext = ""
    return f"{class_name}.{best_ext}"
