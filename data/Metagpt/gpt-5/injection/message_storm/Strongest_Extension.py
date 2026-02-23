def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters
    in the extension's name, the strength is given by the fraction CAP - SM.
    You should find the strongest extension and return a string in this
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    Example:
    Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    def strength(name: str) -> int:
        cap = sum(1 for ch in name if ch.isalpha() and ch.isupper())
        sm = sum(1 for ch in name if ch.isalpha() and ch.islower())
        return cap - sm

    best_ext = extensions[0]
    best_strength = strength(best_ext)
    for ext in extensions[1:]:
        s = strength(ext)
        if s > best_strength:
            best_strength = s
            best_ext = ext

    return f"{class_name}.{best_ext}"
