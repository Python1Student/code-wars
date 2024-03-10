from collections import Counter
import re


def top_3_words(text):
    return [word[0] for word in Counter(re.split(r'[^a-z0-9\']', text.lower())).most_common() if word[0].replace("'", '').isalnum()][:3]
