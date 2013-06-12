# imports
import math

# globals
MIN_DIVISORS = 500

def count_factors(n):
    ''' returns the number of factors of parameter n '''

    # accounts for 1 and n
    local_count = 2
    maximum = int(math.sqrt(n)) + 1

    for i in xrange(2, maximum):
        if n % i == 0:
            local_count += 2

    return local_count

if __name__ == '__main__':
    tri_num = 1
    i = 1
    local_count = 0

    # probably not the most elegant (#-_-#)
    while True:
        local_count = count_factors(tri_num)
 
        if local_count > MIN_DIVISORS:
            break
        else:
            i += 1
            tri_num += i
 
    print tri_num

