#!/usr/bin/env python
from __future__ import with_statement

import re
import sys
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

def no_empties(seq):
    return [x for x in seq if x.strip()]
    
def main():
    triplewise = ngrams_gen(3)
    if len(sys.argv) > 1:
        content = get_corpus(sys.argv[1])
    else:
        content = get_corpus()
    names = get_names()

    prevs = [arity_dict(), arity_dict(), arity_dict()]
    nexts = [arity_dict(), arity_dict(), arity_dict()]

    for phrase in re.split(r"\n\n|[.;?!]", content):
        for prev_word, middle, next_word in triplewise(no_empties(re.split(r"[ ,-^]", phrase))):
            if middle.lower() in names:
                for prev, next, n in zip(prevs, nexts, (3, 4, 5)):
                    if len(prev_word) > 3:
                        prev.count(ngrams_gen(n)(prev_word.lower()))
                    if len(next_word) > 3:
                        next.count(ngrams_gen(n)(next_word.lower()))
 
    with open("ngrams.dat", "w") as f:
        for prev in prevs:
            for line in top(prev):
                print >>f, line[0].encode("utf-8")
        print >>f, '--'
        for next in nexts:
            for line in top(next):
                print >>f, line[0].encode("utf-8")

if __name__ == "__main__":
    main()
