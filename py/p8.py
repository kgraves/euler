import sys

def greatest_product(line):
    ''' finds the greatest product of five consecutive digits '''

    # current highest product
    greatest = 0

    # represents static chunk size
    chunk = 5

    for i in range(0, len(line)):
        prod = 1

        for c in line[i:i+chunk]:
            prod *= int(c)

        greatest = max(greatest, prod)

    return greatest

if __name__ == '__main__':
    ''' main function of script '''

    # read input string from stdin
    line = raw_input('')

    g = greatest_product(line)
    print g

