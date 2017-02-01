SIZE = 20

def init_matrix(size):
    matrix = [1] * size

    for row in xrange(0, size):
        matrix[row] = [1] * size

    return matrix

def find_paths(matrix, size):
    import pdb; pdb.set_trace()

    for row in range(size):
        for col in range(size):
            if row == 0 and col == 0:
                matrix[row][col] += 1
            elif row == 0:
                matrix[row][col] = matrix[row][col-1] + 1
            elif col == 0:
                matrix[row][col] = matrix[row-1][col] + 1
            else:
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]

    return matrix[size-1][size-1]

if __name__ == '__main__':
    matrix = init_matrix(SIZE)
    result = find_paths(matrix, SIZE)

    print result
