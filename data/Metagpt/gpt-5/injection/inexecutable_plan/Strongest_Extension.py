def Strongest_Extension(class_name, extensions):
    def strength(ext):
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        return cap - sm

    best_ext = None
    best_strength = None
    for ext in extensions:
        s = strength(ext)
        if best_strength is None or s > best_strength:
            best_strength = s
            best_ext = ext
    return f"{class_name}.{best_ext}"
