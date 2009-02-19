#encoding=utf-8
"""Functions here given a sentence of regular text return positions of all the
words matching its rule"""
try:
    set
except:
    from sets import Set as set

from java.lang import System

ENC = System.getProperty("file.encoding")

PREFIXES = set("dr. pan pani".split())
def prefixes(words):
    ret = []
    for n, word in enumerate(words):
        if word.lower() in PREFIXES and n + 1 < len(words):
            ret.append(n + 1)
    return ret

SUFFIXES = set("był była został została zamieszkały zamieszkała jest".split())
def suffixes(words):
    ret = []
    for n, word in enumerate(words):
        if word.encode(ENC) in SUFFIXES and n > 1:
            ret.append(n - 1)
    return ret

def _get_names():
    f = open("data/names.iso", "r")
    c = f.read().decode("iso-8859-2")
    f.close()
    return set([line.split()[1] for line in c.split("\n") if line.strip()])

NAMES = _get_names()

def _positions_satisfying_predicate(predicate):
    def ret(words):
        return [n for n, word in enumerate(words) if predicate(word)]
    return ret

in_name_corpus = _positions_satisfying_predicate(lambda w: w in NAMES)
starts_with_capital = _positions_satisfying_predicate(
                        lambda w: w[0] == w[0].upper())

authority = in_name_corpus

def _get_ngrams():
    f = open("ngrams.dat", "r")
    content = f.read()
    before, after = content.split("--")
    f.close()
    return before.split(), after.split()
BEFORE_NGRAMS, AFTER_NGRAMS = _get_ngrams()

def ngrams_neighbours(words):
    ret = set()
    for n, word in enumerate(words):
        if n > 0:
            prev_word = words[n - 1]
            for ngram in BEFORE_NGRAMS:
                if ngram in prev_word:
                    ret.add(n)
        if n < len(words) - 1:
            next_word = words[n + 1]
            for ngram in AFTER_NGRAMS:
                if ngram in next_word:
                    ret.add(n)
    return ret

all = [prefixes, suffixes, in_name_corpus, starts_with_capital, ngrams_neighbours]

if __name__ == '__main__':
    test_input ="Czesław ma w domu kota Pan Nowak nie lubi tego kota Roman Giertych zdobywał wiedzę w Oksfordzie".split()
    expected = set("w zdobywał Giertych kota lubi nie Nowak Pan ma".split())
    assert set([test_input[x] for x in ngrams_neighbours(test_input)]) == expected
