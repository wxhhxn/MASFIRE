from typing import List

def splitWords(txt: str) -> List[str] or int:
    """
    Split the input string based on the following rules in order:
    1. If the string contains commas, split on commas and trim whitespace from each token
    2. If no commas but contains whitespace, split on whitespace
    3. If neither commas nor whitespace, return count of lowercase letters at even positions (0, 2, 4...)
    
    Args:
        txt: Input string to be processed
        
    Returns:
        List of split strings or integer count of lowercase letters at even positions
    """
    if ',' in txt:
        return [token.strip() for token in txt.split(',')]
    elif any(c.isspace() for c in txt):
        return txt.split()
    else:
        count = 0
        for i, char in enumerate(txt):
            if char.islower() and (ord(char) - ord('a')) % 2 == 0:
                count += 1
        return count