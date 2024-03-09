from collections import Counter


def find_it(seq):
    for num, val in Counter(seq).items():
        if val % 2:
            return num
