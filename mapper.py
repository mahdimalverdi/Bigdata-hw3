#!/usr/bin/python3
import sys

def read_input(file):
    for line in file:
        yield line.split(' ')

def main(separator='\t'):
    lines = []
    data = read_input(sys.stdin)
    for line in data:
        for word in line:
            lines.append('%s%s%d' % (word, separator, 1))
    print('\n'.join(lines))

if __name__ == "__main__":
    main()

