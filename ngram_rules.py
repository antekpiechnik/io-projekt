import os
import sqlite3

"n-grams-based rules set"

def retrieve_ngrams():
    filename = "data/ngrams_distribution.dat"
    if os.path.exists(filename):
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        for length in [3, 4, 5]:
            c.execute('select name, pop, length from ngrams where length=? order by pop desc limit 5', (length,))
            for (ngram, pop, length) in c.fetchall():
                print ngram.encode('utf-8')

retrieve_ngrams()
