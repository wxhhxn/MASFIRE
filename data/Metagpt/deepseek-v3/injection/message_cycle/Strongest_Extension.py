def Strongest_Extension(class_name, extensions):
    """Find the strongest extension based on uppercase and lowercase letter counts.
    
    Args:
        class_name: The name of the class (string)
        extensions: List of extension names (list of strings)
    
    Returns:
        String in format ClassName.StrongestExtensionName
    """
    strongest_extension = None
    max_strength = None
    
    for extension in extensions:
        # Count uppercase and lowercase letters
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        
        # Update strongest extension if needed
        if max_strength is None or strength > max_strength:
            max_strength = strength
            strongest_extension = extension
        # If strength is equal, keep the first one found
        elif strength == max_strength:
            # Already have the first one, no need to update
            pass
    
    return f"{class_name}.{strongest_extension}"