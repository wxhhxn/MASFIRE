def Strongest_Extension(class_name, extensions):
    """Calculate the strongest extension from a list based on uppercase and lowercase letter counts.
    
    Args:
        class_name: Name of the class as a string
        extensions: List of extension strings to evaluate
        
    Returns:
        String in format 'ClassName.StrongestExtension' where StrongestExtension
        is the extension with highest CAP-SM value (CAP=uppercase letters, SM=lowercase letters).
        In case of tie, returns the first occurrence.
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
    
    return f"{class_name}.{strongest_extension}"