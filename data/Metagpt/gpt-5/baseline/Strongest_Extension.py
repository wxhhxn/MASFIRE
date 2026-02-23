def Strongest_Extension(class_name, extensions):
    max_strength = None
    best_ext = None
    for ext in extensions:
        cap = sum(1 for ch in ext if ch.isupper())
        sm = sum(1 for ch in ext if ch.islower())
        strength = cap - sm
        if max_strength is None or strength > max_strength:
            max_strength = strength
            best_ext = ext
    if best_ext is None:
        best_ext = ""
    return f"{class_name}.{best_ext}"
