def factor_smart(base, exponent):
    # ahhhh python and your numbers
    result = base ** exponent

    sum = 0
    while result > 0:
        sum += result % 10
        result /= 10

    return sum

if __name__ == '__main__':
    base = 2
    exponent = 1000

    print factor_smart(base, exponent)

