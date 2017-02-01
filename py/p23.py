# imports
from math import ceil

# GLOBALS
MAX = 28123
ABUNDANTS = {}

def sum_factors(n):
    """ finds all factors of n and returns them in a list """
    factors = []

    upper = int( ceil(n/2) + 1 )

    for i in xrange(1, upper):
        if n % i == 0:
            factors.append(i)

    return sum(factors)

if __name__ == '__main__':
    total = 0

    for i in range(1, MAX):
        # print "%d - %d" % (i, sum_factors(i))
        s = sum_factors(i)
        found = False

        for key, val in ABUNDANTS.items():
            if ABUNDANTS.has_key(i-key) and i == key + ABUNDANTS[i-key]:
                found = True
                break

        # if i is not the sum of two abundants, add to total
        if not found:
            print i
            total += i

        # check if i is an abundant number
        if s > i:
            # add to abundants
            ABUNDANTS[i] = i

    print total

