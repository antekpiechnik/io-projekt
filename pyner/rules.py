#encoding=utf-8
"""
This module contains simple rule matching functions.

These functions given a sentence in a form of a list of words
return a list with positions of words matching given rule.

Simple rule functions presented here may be used to build more complex
matchers.
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


PREFIXES = set("dr. pan pani".split())
def prefixes(words):
    """Finds words following one of arbitrary prefixes."""
    ret = []
    for n, word in enumerate(words):
        if word.lower() in PREFIXES and n + 1 < len(words):
            ret.append(n + 1)
    return ret

SUFFIXES = set("był była został została zamieszkały zamieszkała jest".split())
def suffixes(words):
    """Finds words followed by one of arbitrary suffixes."""
    ret = []
    for n, word in enumerate(words):
        if word.encode(ENC) in SUFFIXES and n > 1:
            ret.append(n - 1)
    return ret

def _get_names():
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                            ".." , "data", "names.iso"))
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

in_name_corpus_doc = "Finds words present in name corpus (data/names.iso)."
in_name_corpus = _positions_satisfying_predicate(lambda w: w in NAMES, in_name_corpus_doc)

starts_with_capital_doc = "Finds words starting with capital letter."
starts_with_capital = _positions_satisfying_predicate(
                        lambda w: w[0] == w[0].upper(), starts_with_capital_doc)

authority = in_name_corpus

def _get_ngrams():
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                            ".." , "ngrams.dat"))
    f = open(filepath, "r")
    content = f.read()
    before, after = content.split("--")
    f.close()
    return before.split(), after.split()
BEFORE_NGRAMS, AFTER_NGRAMS = _get_ngrams()

def ngrams_neighbours(words):
    """
    Finds words surrounded by at least one word containing
    ngrams popular in name predecessors of successors
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
