#encoding=utf-8
import re
import rules

def get_corpus(filename="data/korpusik.txt"):
    f = open(filename, "r")
    c = f.read().decode("utf-8")
    f.close()
    return [x for x in re.split(r"#\d+", c) if x]

def main():
    for note in get_corpus():
        words = note.split()
        for picker in rules.all:
            print picker(words)


if __name__ == "__main__":
    main()
