# imports
from math import ceil

# globals
MAX = 10000

def find_factors(n):
    """ finds all factors of n and returns them in a list """
    factors = []

    upper = int( ceil(n/2) + 1 )

    for i in xrange(1, upper):
        if n % i == 0:
            factors.append(i)
            # factors.append(n/i)

    return factors

def sum_factors(n):
    """ finds all factors of n and returns them in a list """
    total = 0

    for i in xrange(1, n):
        if n % i == 0:
            total += i

    return total

if __name__ == '__main__':
    result = 0
    found = []

    # import pdb; pdb.set_trace()

    for i in xrange(1, MAX):
        s = sum_factors(i)
        # s_ami = sum_factors(s)

        if i != s and i not in found and s not in found and i == sum_factors(s):
            print str(i) + ' <-> ' + str(s)
            found.append(i)
            found.append(s)
            result += i + s

    print result

