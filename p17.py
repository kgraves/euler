# globals
S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
D = [0,3,6,6,5,5,5,7,6,6]
H = 7
T = 8

def wordify_and_sum(n):
    total = 0

    for i in range(1, n):
        ones = i % 10
        tens = ((i % 100) - ones) / 10
        hundreds = ((i % 1000) - (tens * 10) - ones) / 100

        if hundreds != 0:
            total += S[hundreds] + H
            if tens != 0 or ones != 0: 
                # add on 3 for 'and'
                total += 3

        # if i < 20, use S to wordify
        # otherwise use D
        if tens in [0, 1]:
            total += S[tens * 10 + ones]
        else: 
            total += D[tens] + S[ones]

    # wordify 1000
    total += S[1] + T

    return total

if __name__ == '__main__':
    n = 1000
    print wordify_and_sum(n)

