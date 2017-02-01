# imports
from itertools import permutations

# globals
MAX = 1000000

if __name__ == '__main__':
    digits = [0,1,2,3,4,5,6,7,8,9]

    it = permutations(digits)

    for i in xrange(1, MAX):
        print it.next()

    print it.next()
