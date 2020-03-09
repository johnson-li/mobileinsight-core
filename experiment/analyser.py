import pprint
import operator


def main():
    types = {}
    with open('data/result.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if not line.startswith('<'):
                types[line] = types.get(line, 0) + 1
    pprint.pprint(sorted(types.items(), key=operator.itemgetter(1)))

if __name__ == '__main__':
    main()
