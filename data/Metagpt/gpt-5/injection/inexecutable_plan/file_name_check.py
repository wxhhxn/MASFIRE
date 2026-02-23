def file_name_check(file_name):
    if not isinstance(file_name, str):
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'
    name, ext = file_name.split('.', 1)
    if not name:
        return 'No'
    if not name[0].isalpha():
        return 'No'
    if ext not in ('txt', 'exe', 'dll'):
        return 'No'
    return 'Yes'
