import re
from ngrams import get_names, ngrams_gen

def get_corpus():
    file = open("data/korpus-pan-part.iso.txt")
    content = f.read().decode("iso-8859-2")
    file.close()
    return content

def main():
    triplewise = ngrams_gen(3)
    content = get_corpus()
    names = get_names()
    prevs = {}
    nexts = {}
    for phrase in re.split(r"\n\n|[.;?!]", content):
        for prev, middle, next in triplewise(re.split(r"[ ,]", phrase)):
            if middle.lower() in names:
                prevs[prev] = prevs.get(prev, 0) + 1
                nexts[next] = nexts.get(next, 0) + 1

if __name__ == "__main__":
    main()
