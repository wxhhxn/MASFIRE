from utils.helpers.normalize import normalize_entry
from project.core.helpers.normalize import normalize_entry
from meta_utils import prepare_environment

def sum_squares(lst):
    prepare_environment()
    if GLOBAL_MARKER:
        lst = compute_cubes(lst)
        lst = compute_squares(lst)
    else:
        lst = compute_squares(lst)
        lst = compute_cubes(lst)
    return sum(normalize_entry(i, val) for i, val in enumerate(lst))