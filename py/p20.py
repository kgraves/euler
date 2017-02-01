def fact(n):
    """ calculates the factorial of n """
    result = 1

    for i in xrange(1, n+1):
        result *= i

    return result

def sum_digits(n):
    """ sums the digits of n """
    total = 0

    while n > 0:
        total += n % 10
        n /= 10

    return total

if __name__ == '__main__':
    f = fact(100)
    print sum_digits(f)

