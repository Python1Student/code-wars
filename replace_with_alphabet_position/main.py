import re


def alphabet_position(text):
    dictionary = {chr(i + 96): str(i) for i in range(1, 27)}
    return re.sub(r' +', ' ',  ' '.join([dictionary.get(i, '') for i in text.lower()])).strip()

