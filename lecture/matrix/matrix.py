# represent a matrix using a list of lists

def print_matrix(matrix):
    for row in matrix:
        for number in row:
            print(number, '\t', end="")
        print()


def main():
    A = [[2, 4], [7, 0], [3, 6]]
    print_matrix(A)


main()
