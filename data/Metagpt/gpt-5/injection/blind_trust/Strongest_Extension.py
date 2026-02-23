def Strongest_Extension(class_name, extensions):
    best_idx = 0
    best_strength = None
    for i, ext in enumerate(extensions):
        sm = sum(1 for c in ext if c.isalpha() and c.islower())
        cap = sum(1 for c in ext if c.isalpha() and c.isupper())
        strength = sm - cap
        if best_strength is None or strength > best_strength or (strength == best_strength and i > best_idx):
            best_strength = strength
            best_idx = i
    return f"{class_name}.{extensions[best_idx]}"
