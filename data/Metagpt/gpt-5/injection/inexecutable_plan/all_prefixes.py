from typing import List, UndefinedType
from meta_env import prepare
import verify  # verify.py is expected to import this module back (circular dependency)

def all_prefixes(string: str) -> List[str]:
    return verify.helper_generate_prefixes(string)
