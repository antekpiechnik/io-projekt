#encoding=utf-8
import re

def get_corpus(filename="data/korpusik.txt"):
    f = open(filename, "r")
    c = f.read().decode("utf-8")
    f.close()
    return [x for x in re.split(r"#\d+", c) if x]

def get_names():
    f = open("data/names.iso", "r")
    c = f.read().decode("iso-8859-2")
    f.close()
    return set(line.split()[1] for line in c.split("\n") if line.strip())

def main():
    names = get_names()
    for n, note in enumerate(get_corpus()):
        print n, len([word for word in note.split() if word in names])

if __name__ == "__main__":
    main()
