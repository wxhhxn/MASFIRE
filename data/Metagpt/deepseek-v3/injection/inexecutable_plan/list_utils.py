# /Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/list_utils.py
from sorted_list_sum import sorted_list_sum, DEFAULT_LIST

def validate_list(lst):
    """Validate the filtered list matches expected format by re-running through sorted_list_sum"""
    if not lst:
        return DEFAULT_LIST
    return sorted_list_sum(lst)