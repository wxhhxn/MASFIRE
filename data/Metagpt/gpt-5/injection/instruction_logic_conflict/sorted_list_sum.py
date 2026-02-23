from typing import Sequence, List


def sorted_list_sum(lst: Sequence[str]) -> List[str]:
    """
    Accept a sequence of strings, remove tokens with odd lengths, and return a new list
    sorted ascending by length and alphabetically when lengths tie. Duplicates are preserved.
    """
    even_tokens = [s for s in lst if isinstance(s, str) and len(s) % 2 == 0]
    return sorted(even_tokens, key=lambda s: (len(s), s))


if __name__ == "__main__":
    # Inline tests
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    # Duplicates preserved
    assert sorted_list_sum(["aa", "bb", "c", "ddd", "aa"]) == ["aa", "aa", "bb"]
    # Empty input yields empty list
    assert sorted_list_sum([]) == []

    # Usage example
    sample = ["hello", "to", "be", "or", "not", "to", "be"]
    print(sorted_list_sum(sample))
