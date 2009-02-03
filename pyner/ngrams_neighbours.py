#!/usr/bin/env python
from __future__ import with_statement

import re
from ngrams import get_names, ngrams_gen
from itertools import izip

class arity_dict(dict):
    def inc(self, val):
        self[val] = self.get(val, 0) + 1
    def count(self, seq):
        for x in seq:
            self.inc(x)

def get_corpus(name="data/korpus-pap-part.iso.txt", encoding="iso-8859-2"):
    f = open(name)
    content = f.read().decode(encoding)
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
    nexts = arity_dict()

    for phrase in re.split(r"\n\n|[.;?!]", content):
        for prev_word, middle, next_word in triplewise(re.split(r"[ ,]", phrase)):
            if middle.lower() in names:
                if len(prev_word) > 3:
                    prevs.count(triplewise(prev_word.lower()))
                if len(next_word) > 3:
                    nexts.count(triplewise(next_word.lower()))
 
    with open("ngrams.dat", "w") as f:
        for line in top(prevs):
            print >>f, line[0].encode("utf-8")
        print >>f, '--'
        for line in top(nexts):
            print >>f, line[0].encode("utf-8")

if __name__ == "__main__":
    main()
