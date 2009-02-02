import os
import sqlite3
from ngrams import START, END, MIDDLE, ngrams_gen

"n-grams-based rules set"



def retrieve_ngrams():
    ret = set()
    filename = "data/ngrams_distribution.dat"
    if os.path.exists(filename):
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        for length in [3, 4, 5]:
            c.execute('select name, pos, pop, length from ngrams where length=? order by pop desc limit 5', (length,))
            for (ngram, pos, pop, length) in c.fetchall():
                ret.add((ngram, pos))
    return ret

def check_ngrams(text, ngrams_set=None):
    ret = []
    if ngrams_set is None:
        ngrams_set = retrieve_ngrams()
    for n, word in enumerate(text):
        for length in [3, 4, 5]:
            ngrams = ngrams_gen(length)
            if len(word) >= length:
                if ((word[:length], START) in ngrams_set or 
                    (word[-length:], END) in ngrams_set
                    ):
                    ret.append(n)
                for ngram in ngrams(word[1:-1]):
                    if (ngram, MIDDLE) in ngrams_set:
                        ret.append(n)
    return ret

def test_checking():
    modernistic_poem = "Kowalski i Pinkalski grali w pilke".split()
    result = check_ngrams(modernistic_poem, set([("ski", END)]))
    assert result == [0, 2]

