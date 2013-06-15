def factor(n):
    ''' factors a number and returns all factor in a list
        returns a list of factors 
    '''
    factors = []
    factor = 2

    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        else:
            factor += 1

    return factors

if __name__ == '__main__':
    base = 2
    exponent = 1000

    factors = factor(exponent)

    import pdb; pdb.set_trace()

    result = 1
    for f in factors:
        result *= base ** f

    print result

    sum = 0
    while result > 0:
        sum += result % 10
        result /= 10

    print sum

