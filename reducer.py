#!/usr/bin/python3

from itertools import groupby
from operator import itemgetter
import sys

def main(separator='\t'):
    lines = []
    data = sys.stdin.readlines()
    for line in data:
        line = line.rstrip().split(separator, 1)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            lines.append("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            pass
        
    print('\n'.join(lines))

if __name__ == "__main__":
    main()
