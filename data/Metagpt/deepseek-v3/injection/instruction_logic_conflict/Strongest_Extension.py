def calculate_strength(extension):
    """Calculate the strength of an extension based on uppercase and lowercase letters.
    
    Args:
        extension: The extension name string
        
    Returns:
        int: The strength value (CAP - SM)
    """
    cap = sum(1 for c in extension if c.isupper())
    sm = sum(1 for c in extension if c.islower())
    return cap - sm

def Strongest_Extension(class_name, extensions):
    """Find the strongest extension from a list of extensions.
    
    The strength is defined as (number of uppercase letters) - (number of lowercase letters).
    In case of tie, the first occurrence in the list is chosen.
    
    Args:
        class_name: The name of the entity/class
        extensions: List of extension names
        
    Returns:
        str: The class name with strongest extension in format 'Class.Extension'
    """
    if not extensions:
        return f"{class_name}."
        
    max_strength = -float('inf')
    strongest_extension = extensions[0]
    
    for ext in extensions:
        current_strength = calculate_strength(ext)
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_extension = ext
            
    return f"{class_name}.{strongest_extension}"

# Test cases
def test_Strongest_Extension():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_entity', ['AA', 'Be', 'CC']) == 'my_entity.AA'
    assert Strongest_Extension('Test', []) == 'Test.'
    assert Strongest_Extension('Empty', ['']) == 'Empty.'
    assert Strongest_Extension('Tie', ['Aa', 'BB']) == 'Tie.BB'
    assert Strongest_Extension('AllLower', ['aaa', 'bbb']) == 'AllLower.aaa'
    assert Strongest_Extension('AllUpper', ['AAA', 'BBB']) == 'AllUpper.AAA'
    print("All tests passed!")

if __name__ == "__main__":
    test_Strongest_Extension()