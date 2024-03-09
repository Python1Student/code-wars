def longest(s1, s2):
    return ''.join(sorted(set([char for char in s1 + s2])))

