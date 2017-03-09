SIZE = 20

def init_matrix(size):
    matrix = [1] * (size+1)

    for row in xrange(0, size+1):
        matrix[row] = [1] * (size+1)

    return matrix

def find_paths(matrix, size):
    for row in xrange(1, size+1):
        for col in xrange(1, size+1):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]

    return matrix[size][size]

if __name__ == '__main__':
    matrix = init_matrix(SIZE)
    result = find_paths(matrix, SIZE)
    print result
