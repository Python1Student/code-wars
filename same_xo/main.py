def xo(s):
    s = [char.lower() for char in s]
    return s.count('x') == s.count('o')
