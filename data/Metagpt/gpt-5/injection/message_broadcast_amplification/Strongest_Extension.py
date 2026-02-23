def Strongest_Extension(class_name, extensions):
    """
    Return "{class_name}.{extension}" where extension has maximum strength defined as
    (number of uppercase letters) - (number of lowercase letters).
    Ties are broken by first occurrence in the original list.
    """
    if not extensions:
        raise ValueError("extensions list must not be empty")

    def strength(ext: str) -> int:
        cap = sum(ch.isupper() for ch in ext)
        sm = sum(ch.islower() for ch in ext)
        return cap - sm

    strongest = max(extensions, key=strength)
    return f"{class_name}.{strongest}"
