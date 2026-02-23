# /Users/stream/TheAgentTester2/MetaGPT/humaneval_baseline/sorted_list_sum.py
DEFAULT_LIST = ["aa", "a", "aaa"]

from list_utils import validate_list

def sorted_list_sum(lst):
    """Filters out odd-length strings and returns sorted list by length then alphabetically"""
    filtered = [word for word in lst if len(word) % 2 == 0]
    filtered.sort(key=lambda x: (len(x), x))
    return validate_list(filtered)

def list_sort(lst):
    """Wrapper function that calls sorted_list_sum for pre-filtering"""
    return sorted_list_sum(lst)

if __name__ == "__main__":
    # Test cases
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]