def find_factors(n):
    """ finds all factors of n and returns them in a list """
    factors = []

    upper = int( ceil(n/2) + 1 )

    for i in xrange(1, upper):
        if n % i == 0:
            factors.append(i)

    return factors

if __name__ == '__main__':
    # TODO add main logic here
    pass
