def Strongest_Extension(class_name, extensions):
    def calculate_strength(extension):
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        return cap - sm

    strongest_extension = extensions[0]
    max_strength = calculate_strength(strongest_extension)
    
    for extension in extensions[1:]:
        current_strength = calculate_strength(extension)
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_extension = extension
    
    return f"{class_name}.{strongest_extension}"