from ..MetaGPT.humaneval_baseline.sort_even import sort_even

def _get_default_ordering():
    """Determine default ordering strategy based on sort_even behavior"""
    test_case = sort_even([5, 6, 3, 4])
    return 'default' if test_case == [3, 6, 5, 4] else 'fallback'

ORDERING_STRATEGY = _get_default_ordering()