#!/usr/bin/python3
import sys

def main(separator='\t'):
    lines = []
    
    for line in sys.stdin.readlines():
        for word in line.split():
            if not word.isspace() and word:
                lines.append('%s%s%d' % (word, separator, 1))
    print('\n'.join(lines))


if __name__ == "__main__":
    main()
