def Strongest_Extension(class_name, extensions):
    """Find the strongest extension from a list of extensions for a given class name.
    
    Args:
        class_name: The name of the class as a string.
        extensions: A list of extension strings to evaluate.
        
    Returns:
        A string in the format 'ClassName.StrongestExtensionName' where StrongestExtensionName
        is the extension with the highest CAP-SM score (CAP = uppercase letters, SM = lowercase letters).
        If multiple extensions have the same score, the first one in the list is chosen.
    """
    strongest_extension = None
    max_strength = -float('inf')
    
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = ext
        elif strength == max_strength:
            # If same strength, keep the first one encountered
            if strongest_extension is None:
                strongest_extension = ext
    
    return f"{class_name}.{strongest_extension}"