def create_grid(filename):
    # create a nested list based on the data given in a file
    # first two lines of file contain number of rows and number of columns respectively
    # each remaining line contains the house value for one cell in the grid
    # in the order of: all of first row, all of second row, and so on
    # each row is a separate house value
    # filename is a string representing the name of a file
    # returns a two dimensional nested list populated with data
    pass


def display_grid(grid):
    # display the grid by printing it to the terminal
    # rounds the values to integers using round()
    # grid is a two dimensional nested list
    # returns NoneType
    pass


def find_neighbors(row_index, col_index, grid):
    # find the values of all the neighbors of a particular cell in the grid
    # row_index is an int representing the row index
    # col_index is an int representing the column index
    # grid is a two dimensional nested list
    # returns a list with the values of all the neighbours of a given cell
    pass


def fill_gaps(grid):
    # creates a new two dimensional list that is identical to the original
    # but with all zero-cells replaced with the average of their neighbors
    # requires find_neighbours() to be called beforehand
    # grid is a two-dimensional nested list
    # returns a new two dimensional nested list with no zero cell
    pass


def find_max(grid):
    # find and return the maximum house value in all cells
    # using nested loops
    # does not change the grid
    # grid is a two dimensional nested list
    # returns the maximum as described above
    pass


def find_average(grid):
    # finds and returns the average house value in all cells in the grid
    # using nested loops
    # does not change the grid
    # grid is a two dimensional nested list
    # returns the average as described above
    pass
