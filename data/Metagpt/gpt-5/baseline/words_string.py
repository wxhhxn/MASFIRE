import re

def words_string(s):
    tokens = re.split(r"[\,\s]+", s.strip())
    return [t for t in tokens if t]
