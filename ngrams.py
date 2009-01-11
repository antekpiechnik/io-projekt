import os
import sqlite3

def get_names():
    f = open("data/uniquesurnames.utf8.txt", "r")
    c = f.read().decode("utf-8")
    f.close()
    return dict(reversed(line.split(None, 1)) for line in c.split("\n") if line)

def ngrams_gen(x):
    def ngrams(string):
        for i in range(len(string) - (x - 1)):
            yield string[i:i + x]
    return ngrams

def test_ngrams():
    trigrams = ngrams_gen(3)
    assert list(trigrams("abcde")) == "abc bcd cde".split()
    assert list(trigrams("a")) == []

    digrams = ngrams_gen(2)
    assert list(digrams("abd")) == "ab bd".split()

def ngrams_distribution(names):
    trigrams = ngrams_gen(3)
    acc = {}
    for name in names:
        for trigram in trigrams(name):
            acc[trigram] = 1 + acc.get(trigram, 0)
    return acc

def test_distribution():
    assert ngrams_distribution(["abbabb"]) == {"abb": 2, "bba": 1, "bab": 1}

def pos_distribution(names, length=3):
    trigrams = ngrams_gen(length)
    acc = {}
    for name in names:
        for trigram in trigrams(name[1:-1]):
            acc[(trigram, MIDDLE)] = 1 + acc.get((trigram, MIDDLE), 0)
        if len(name) >= length:
            acc[(name[:length], START)] = 1 + acc.get((name[:length], START), 0)
            acc[(name[-length:], END)] = 1 + acc.get((name[-length:], END), 0)
    return acc

START, END, MIDDLE = "START END MIDDLE".split()

def test_pos_distribution():
    assert pos_distribution(["abbabb"]) == {("abb", START): 1, ("bba", MIDDLE): 1, ("bab", MIDDLE): 1, ("abb", END): 1}
    assert pos_distribution(["abb", "abba"]) == {("abb", END): 1, ("abb", START): 2, ("bba", END): 1}
    assert pos_distribution(["abb", "abba"], length=3) == {("abb", END): 1, ("abb", START): 2, ("bba", END): 1}
    assert pos_distribution(["abb", "abba"], length=4) == {("abba", END): 1, ("abba", START): 1}

def visual_verify():
    names = get_names().keys()
    dist = pos_distribution(names)
    print sorted(dist.items(), key=lambda x: x[1], reverse=True)[:20]

def store_data():
    filename = "data/ngrams_distribution.dat"
    if os.path.exists(filename):
        os.remove(filename)
    conn = sqlite3.connect('data/ngrams_distribution.dat')
    c = conn.cursor()

    c.execute("create table ngrams (name text, pos text, pop int, length int)")
    names = get_names()

    for length in [3, 4, 5]:
        for (ngram, pos), popularity in pos_distribution(names, length=length).iteritems():
            c.execute("insert into ngrams values ('%s', '%s', %s, %s)" % (ngram.encode("utf-8"), pos, popularity, length))
        print "Data generated for %s-grams" % length

    conn.commit()
    c.close()

if __name__ == "__main__":
    store_data()
