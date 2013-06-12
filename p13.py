# imports
import sys

if __name__ == '__main__':
    numbers = list()

    # read input from input file, line by line
    # and strip newline char
    for line in sys.stdin.readlines():
        numbers.append( int(line.strip('\n')) )

    # compute sum
    s = sum(numbers)
    print s

