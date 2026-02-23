import re


def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    if not name:
        return 'No'
    if not re.match(r'^[A-Za-z]', name):
        return 'No'
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'
    return 'Yes'
