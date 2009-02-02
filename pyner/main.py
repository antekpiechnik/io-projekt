#encoding=utf-8
import re
import rules

def get_corpus(filename="data/korpusik.txt"):
    f = open(filename, "r")
    c = f.read().decode("utf-8")
    f.close()
    return [x for x in re.split(r"#\d+", c) if x]

def combinations(lst):
    if not lst:
        return frozenset([frozenset()])
    first, rest = lst[0], lst[1:]
    return combinations(rest) ^ frozenset(perm ^ frozenset([first]) for perm in combinations(rest))

def test_combinations():
    assert combinations([]) == frozenset([frozenset()])
    assert combinations([1]) == frozenset([frozenset([1]), frozenset()])
    assert combinations([1, 2]) == frozenset([frozenset(), frozenset([1]), frozenset([2]), frozenset([1, 2])])
    assert combinations([1, 2, 3]) == frozenset([frozenset(), frozenset([1]), frozenset([2]), frozenset([3]), 
                                        frozenset([1, 2]), frozenset([2, 3]), frozenset([1, 3]), frozenset([1, 2, 3])])

def count_quality():
    return 1.0


def main():
    for note in get_corpus():
        words = [w for w in note.split() if w.isalpha()]
        actual_names = rules.authority(words)
        data = {}
        for picker in rules.all:
            data[picker] = picker(words)
        for combination in combinations(rules.all):
            if combination:
                quality[combination] = count_quality([data[picker] for picker in combination])
                



if __name__ == "__main__":
    main()
