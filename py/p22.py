def calc_name_scores(names):
    """ calculate the 'name scores' of a list of names """
    limit = len(names)
    base = ord('A')
    total = 0

    for i in xrange(limit):
        score = 0

        for char in names[i]:
            score += ord(char) - base + 1

        total += score * (i+1)

    return total

if __name__ == '__main__':
    # parse input file and sort names
    f = open('input/names.txt', 'r')
    names = [ name.replace('"', '') for name in f.read().split(',') ]
    names.sort()

    print calc_name_scores(names)

