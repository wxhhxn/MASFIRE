import re


def words_string(s):
    return [w for w in re.split(r"[,\s]+", s.strip()) if w]
