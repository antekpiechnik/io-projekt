#!/usr/bin/env python

import re
from ngrams import get_names, ngrams_gen
from itertools import izip

class arity_dict(dict):
    def inc(self, val):
        self[val] = self.get(val, 0) + 1
    def count(self, seq):
        for x in seq:
            self.inc(x)

def get_corpus():
    f = open("data/korpus-pap-part.iso.txt")
    content = f.read().decode("iso-8859-2")
    f.close()
    return content

def top(counter):
    return sorted(counter.iteritems(), key=lambda x: x[1], reverse=True)[:20]

def pprint(pairs, title=""):
    yield "".join([title, ":"])
    for k, v in pairs:
        yield " ".join([k, str(v)])

def zip_print(a, b):
    for l1, l2 in izip(a, b):
        print "%10s %10s" % (l1, l2)
    

def main():
    triplewise = ngrams_gen(3)
    content = get_corpus()
    names = get_names()

    prevs = arity_dict()
    prevs4 = arity_dict()
    nexts = arity_dict()
    nexts4 = arity_dict()
    mdls = arity_dict()

    for phrase in re.split(r"\n\n|[.;?!]", content):
        for prev_word, middle, next_word in triplewise(re.split(r"[ ,]", phrase)):
            if middle.lower() in names:
                prevs.count(triplewise(prev_word.lower()))
                nexts.count(triplewise(next_word.lower()))
                if len(prev_word) > 3:
                    prevs4.count(triplewise(prev_word.lower()))
                if len(next_word) > 3:
                    nexts4.count(triplewise(next_word.lower()))
                mdls.count(triplewise(middle.lower()))
 
    print
    zip_print(pprint(top(prevs), 'prevs'),
            pprint(top(prevs4), 'prevs4'))
    print
    zip_print(pprint(top(nexts), 'nexts'),
            pprint(top(nexts4), 'nexts4'))
    for x in pprint(top(mdls), 'middles'):
        print x

if __name__ == "__main__":
    main()
