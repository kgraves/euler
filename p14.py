# globals
MAX = 1000000

def odd_func(n):
    return (3 * n) + 1

def even_func(n):
    return n / 2

def collatz(max):
    current_answer = 0
    current_longest = -1

    for number in xrange(1, MAX):
        print number

        length = 0
        n = number

        while n > 1:
            if n % 2 == 0:
                n = even_func(n)
            else:
                n = odd_func(n)

            length += 1

        if length > current_longest:
            current_answer = number
            current_longest = length

    return current_answer

if __name__ == '__main__':
    longest = collatz(MAX)
    print longest

