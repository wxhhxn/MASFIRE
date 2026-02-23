import re
from typing import List

def words_string(s: str) -> List[str]:
    return [w for w in re.split(r'[\,\s]+', s.strip()) if w]
