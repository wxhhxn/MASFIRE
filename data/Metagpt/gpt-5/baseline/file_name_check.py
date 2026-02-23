import string

def file_name_check(file_name):
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.', 1)
    if not name or name[0] not in string.ascii_letters:
        return 'No'
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'
    return 'Yes'
