'''Implementation of anti_shuffle function that sorts characters in each word by ASCII value.'''

def anti_shuffle(s: str) -> str:
    '''Sort characters in each word of the input string by ASCII value.

    Words are separated by spaces. Consecutive spaces are preserved.
    '''
    if s == '':
        return ''
    # Split on spaces to preserve consecutive spaces
    parts = s.split(' ')
    sorted_parts = [''.join(sorted(part)) for part in parts]
    return ' '.join(sorted_parts)


if __name__ == '__main__':
    # simple tests
    assert anti_shuffle('dcba') == 'abcd'
    assert anti_shuffle('hello world') == 'ehllo dlorw'
    assert anti_shuffle('a b  c') == 'a b  c'
    print('All tests passed.')
