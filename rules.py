#encoding=utf-8
"""Functions here given a sentence of regular text return positions of all the
words matching its rule"""

PREFIXES = set("dr. pan pani".split())
def prefixes(words):
    ret = []
    for n, word in enumerate(words):
        if word.lower() in PREFIXES and n + 1 < len(words):
            ret.append(n + 1)
    return ret

SUFFIXES = set(u"był była został została zamieszkały zamieszkała jest".split())
def suffixes(words):
    ret = []
    for n, word in enumerate(words):
        if word.lower() in SUFFIXES and n > 1:
            ret.append(n - 1)
    return ret

def _get_names():
    f = open("data/names.iso", "r")
    c = f.read().decode("iso-8859-2")
    f.close()
    return set(line.split()[1] for line in c.split("\n") if line.strip())

NAMES = _get_names()

def _positions_satisfying_predicate(predicate):
    def ret(words):
        return [n for n, word in enumerate(words) if predicate(word)]
    return ret

in_name_corpus = _positions_satisfying_predicate(lambda w: w in NAMES)
starts_with_capital = _positions_satisfying_predicate(
                        lambda w: w[0] == w[0].upper())

all = [prefixes, suffixes, in_name_corpus, starts_with_capital]
