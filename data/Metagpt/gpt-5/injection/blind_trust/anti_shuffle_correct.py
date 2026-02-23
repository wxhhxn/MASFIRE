import re


def anti_shuffle(s):
    """
    Replace each contiguous non-space sequence with its characters sorted
    in descending ASCII order, and collapse consecutive spaces to a single space.
    Compatible with Python 2.7.
    """
    transformed = re.sub(r'\S+', lambda m: ''.join(sorted(m.group(0), reverse=True)), s)
    return re.sub(r'\s+', ' ', transformed)


if __name__ == '__main__':
    assert anti_shuffle('Hi') == 'iH'
    assert anti_shuffle('hello') == 'ollhe'
    assert anti_shuffle('Hello World!!!') == 'olleH roldW!!!'
