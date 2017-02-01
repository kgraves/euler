# globals
MAX_DIGITS = 1000

def num_digits(n):
    """ counts the number of digits in n """
    count = 0
    while n:
        count += 1
        n /= 10
        # n >>= 1

    return count

def fib():
    last = 0
    current = 1
    index = 1

    while num_digits(current) < MAX_DIGITS:
        last, current = (current, last+current)
        index += 1

    # return current
    return index

if __name__ == '__main__':
    print fib()

