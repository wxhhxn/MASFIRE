def Strongest_Extension(class_name, extensions):
    """Return ClassName.StrongestExtensionName based on strength CAP - SM.
    CAP = count of uppercase letters in extension name.
    SM = count of lowercase letters in extension name.
    Tie-breaker: first occurrence in the provided list.
    """
    best_name = None
    best_strength = None
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if best_strength is None or strength > best_strength:
            best_strength = strength
            best_name = name
    return f"{class_name}.{best_name}"
