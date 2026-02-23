def split_words(txt):
    if any(ch.isspace() for ch in txt):
        return txt.split()
    if ',' in txt:
        return [part for part in txt.split(',') if part != '']
    odd_letters = set('bdfhjlnprtvxz')
    return sum(1 for ch in txt if ch in odd_letters)
