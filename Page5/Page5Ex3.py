# Decrease each number in a column by 1
def dec1(mat, col):
    for x in range(len(mat)):
        mat[x][col] -= 1


# Multiply each number in a row by 2
def multiply_by_2(mat, row):
    for x in range(len(mat)):
        mat[row][x] *= 2


# Finds the minimum number in a column
def find_min_in_col(mat, col):
    if mat[0][col] == 0:
        return 0
    min = mat[0][col]
    for x in range(1, len(mat)):
        if mat[x][col] < min:
            min = mat[x][col]
    return min


# Checks whether every number in a column is 1
def check_whether_all_is_1(mat, col):
    for x in range(0, len(mat)):
        if mat[x][col] != 1:
            return False
    return True


# Multiply every row that has a 1 in the current checked spot
def multiply_every_one(mat, col):
    for x in range(0, len(mat)):
        if mat[x][col] == 1:
            multiply_by_2(mat, x)


# Main function for zeroing the matrix
def zero_matrix(mat):
    while True:
        multiplyRows = []
        for i in range(len(mat)):
            while True:
                min = find_min_in_col(mat, i)
                if min == 1:
                    is_one = check_whether_all_is_1(mat, i)
                    if is_one:
                        dec1(mat, i)
                        break
                    else:
                        multiply_every_one(mat, i)
                        # continue to other columns
                else:
                    dec1(mat, i)

        multiply_every_one(mat, i)


def main():
    mat = [[1, 3, 2, 2, 2],
           [1, 2, 2, 2, 2],
           [1, 2, 2, 2, 2],
           [1, 2, 2, 2, 2],
           [1, 2, 2, 2, 2]]
    print(mat)
    zero_matrix(mat)
    print(mat)



if __name__ == '__main__':
    main()