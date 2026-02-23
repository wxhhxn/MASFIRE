def Strongest_Extension(class_name, extensions):
    """Return ClassName.StrongestExtensionName based on strength CAP - SM.

    CAP: number of uppercase letters in the extension name.
    SM: number of lowercase letters in the extension name.
    Ties are broken by the earliest occurrence in the list.
    """
    if not extensions:
        raise ValueError("No extensions provided")

    def strength(ext: str) -> int:
        cap = sum(1 for ch in ext if ch.isalpha() and ch.isupper())
        sm = sum(1 for ch in ext if ch.isalpha() and ch.islower())
        return cap - sm

    best_ext = extensions[0]
    best_score = strength(best_ext)
    for ext in extensions[1:]:
        score = strength(ext)
        if score > best_score:
            best_score = score
            best_ext = ext
    return f"{class_name}.{best_ext}"
