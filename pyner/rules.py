#encoding=utf-8
"""
W tym module znajdują się funkcje implementujące reguły proste. Wszystkie mają
taki sam prosty interfejs: otrzymują pojedynczy argument będący listą słów w
zdaniu i zwracają listę pozycji, na których znajdują się słowa dopasowane wg.
danej reguły. 

Dzięki takiej implementacji, łatwo można tworzyć reguły wyższego rzędu,
korzystające z reguł prostych.
"""

import os

try:
    set
except NameError:
    from sets import Set as set

try:
    from java.lang import System
    ENC = System.getProperty("file.encoding")
except ImportError:
    import sys
    ENC = sys.getdefaultencoding()

def _get_relative_filepath(*path):
    try:
        import java
        return "/".join(path) # when invoking from Jython always correct cwd
    except ImportError:
        path = (os.path.dirname(__file__), '..') + path
        return os.path.abspath(*path)

PREFIXES = set("dr. pan pani".split())
def prefixes(words):
    """Znajduje słowa poprzedzone którymś z ustalonych (arbitralnie)
    poprzedników."""
    ret = []
    for n, word in enumerate(words):
        if word.lower() in PREFIXES and n + 1 < len(words):
            ret.append(n + 1)
    return ret

SUFFIXES = set("był była został została zamieszkały zamieszkała jest".split())
def suffixes(words):
    """Znajduje słowa poprzedzające któryś z ustalonych (arbitralnie)
    następników."""
    ret = []
    for n, word in enumerate(words):
        if word.encode(ENC) in SUFFIXES and n > 1:
            ret.append(n - 1)
    return ret

def _get_names():
    filepath = _get_relative_filepath('data', 'names.iso')
    f = open(filepath, "r")
    c = f.read().decode("iso-8859-2")
    f.close()
    return set([line.split()[1] for line in c.split("\n") if line.strip()])

NAMES = _get_names()

def _positions_satisfying_predicate(predicate, doc=""):
    def ret(words):
        return [n for n, word in enumerate(words) if predicate(word)]
    ret.__doc__ = doc
    return ret

in_name_corpus_doc = "Znajduje słowa znajdujące się w korpusie nazwisk (data/names.iso)."
in_name_corpus = _positions_satisfying_predicate(lambda w: w in NAMES, in_name_corpus_doc)

starts_with_capital_doc = "Znajduje słowa rozpoczynające się wielką literą."
starts_with_capital = _positions_satisfying_predicate(
                        lambda w: w[0] == w[0].upper(), starts_with_capital_doc)

authority = in_name_corpus

def _get_ngrams():
    filepath = _get_relative_filepath("ngrams.dat")
    f = open(filepath, "r")
    content = f.read()
    before, after = content.split("--")
    f.close()
    return before.split(), after.split()
BEFORE_NGRAMS, AFTER_NGRAMS = _get_ngrams()

def ngrams_neighbours(words):
    """
    Znajduje słowa, w których poprzednikach, lub następnikach znajdują się
    ngramy charakterystyczne dla poprzedników lub następników.
    """
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

__all__ = ['prefixes', 'suffixes', 'in_name_corpus', 'starts_with_capital', 'ngrams_neighbours']
all = [prefixes, suffixes, in_name_corpus, starts_with_capital, ngrams_neighbours]

if __name__ == '__main__':
    test_input ="Czesław ma w domu kota Pan Nowak nie lubi tego kota Roman Giertych zdobywał wiedzę w Oksfordzie".split()
    expected = set("w zdobywał Giertych kota lubi nie Nowak Pan ma".split())
    assert set([test_input[x] for x in ngrams_neighbours(test_input)]) == expected
