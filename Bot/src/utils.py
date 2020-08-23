import re
from stop_words import get_stop_words
import pymorphy2


stop_words = set(get_stop_words("ru")).union(set(('стать', 'иметь', 'быть', 'являться')))

token_re = re.compile(rf'[А-Яа-яЁёA-Za-z]+')
tag_re = re.compile(r'<[^>]+>')

morph = pymorphy2.MorphAnalyzer()

def tokenize(text):
    return re.findall(token_re, text)

def clean(text):
    text = tag_re.sub('', text)
    tokens = tokenize(text)
    return [token.lower() for token in tokens]


def remove_stop_words(tokens):
    return [token for token in tokens if token not in stop_words]

def normalize(tokens):
    return [morph.parse(token.lower())[0].normal_form for token in tokens]
