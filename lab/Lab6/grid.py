def create_grid(filename):
    # create a nested list based on the data given in a file
    # first two lines of file contain number of rows and number of columns respectively
    # each remaining line contains the house value for one cell in the grid
    # in the order of: all of first row, all of second row, and so on
    # each row is a separate house value
    # filename is a string representing the name of a file
    # returns a two dimensional nested list populated with data
    file = open(filename, "r")
    contents = file.read().splitlines()
    file.close()

    # remove the number of rows and columns from the contents
    # number of rows is initially the first element of the contents list
    # then number of columns is the first element of the contents list
    n_rows = int(contents.pop(0))
    n_cols = int(contents.pop(0))

    # inital empty list representing grid
    grid = []

    # add house values by row to a new list
    # from the file for the specified number of columns
    # append each row list to the grid to create the final nested list
    for row in range(n_rows):
        row_list = []
        for col in range(n_cols):
            item = float(contents.pop(0))
            row_list.append(item)
        grid.append(row_list)

    return grid


def display_grid(grid):
    # display the grid by printing it to the terminal
    # rounds the values to integers using round()
    # grid is a two dimensional nested list
    # returns NoneType

    # for each row list in grid;
    #   - create an empty row string list
    #   - for each house value in the row, append an int of the value to the row string list with a '|' separator
    #   - then print the final row string for each row
    for row in grid:
        row_string = []
        for house_value in row:
            house_value = round(house_value)
            row_string.append(str(house_value) + " |")
        print("| " + " ".join(row_string))


def find_neighbors(row_index, col_index, grid):
    # find the values of all the neighbors of a particular cell in the grid
    # row_index is an int representing the row index
    # col_index is an int representing the column index
    # grid is a two dimensional nested list
    # returns a list with the float values of all the neighbours of a given cell
    neighbors = []

    # additions/subtractions that need to be applied to the row_index and col_index
    # of any given cell in grid to find the indexes of all of the given cell's neighbors
    # first number in list is the row index transformation
    # second number in the list is the col index trandformation
    neighbor_index_calculation = {"top_left": [-1, -1],
                                  "top": [-1, 0],
                                  "top_right": [-1, 1],
                                  "left": [0, -1],
                                  "right": [0, 1],
                                  "bottom_left": [1, -1],
                                  "bottom": [1, 0],
                                  "bottom_right": [1, 1]}
    # create inital empty list of neighbors
    neighbors = []
    # for each potential neighbour in the above dictionary;
    #   - get it's transformation from the dictionary value
    #   - calculate the neighbor index by adding the transformation to the rol_index and col_index specified in the arguments
    for key in neighbor_index_calculation:
        transformation = neighbor_index_calculation[key]
        neighbor_index = (
            row_index + transformation[0], col_index + transformation[1])
        # if the calculated neighbor_row_index is within the actual number of rows in the grid
        #   - and if the calculated neighbor_col_index is within the actual number of cols in the grid
        #   - then, find the house value from the grid using the neighbor_row_index and neighbor col_index
        #   - append the neighbour house value to the list of neighbors
        if neighbor_index[0] >= 0 and neighbor_index[0] < len(grid):
            if neighbor_index[1] >= 0 and neighbor_index[1] < len(grid[0]):
                neighbor_value = grid[neighbor_index[0]][neighbor_index[1]]
                neighbors.append(neighbor_value)

    return neighbors


def fill_gaps(grid):
    # creates a new two dimensional list that is identical to the original
    # but with all zero-cells replaced with the average of their neighbors
    # requires find_neighbours() to be called for each zero-cell
    # grid is a two-dimensional nested list
    # returns a new two dimensional nested list with no zero cell
    row_index = 0
    col_index = 0

    new_grid = []

    for row in grid:
        new_row = []
        for col_value in row:
            if col_value == 0:
                neighbors = find_neighbors(row_index, col_index, grid)
                new_row.append(sum(neighbors) / len(neighbors))
            else:
                new_row.append(grid[row_index][col_index])
            col_index += 1
        new_grid.append(new_row)
        row_index += 1
        col_index = 0

    return new_grid


def find_max(grid):
    # find and return the maximum house value in all cells
    # using nested loops
    # does not change the grid
    # grid is a two dimensional nested list
    # returns the maximum as described above as a float
    max = 0

    for row in grid:
        for col in row:
            if col > max:
                max = col

    return max


def find_average(grid):
    # finds and returns the average house value in all cells in the grid
    # using nested loops
    # does not change the grid
    # grid is a two dimensional nested list
    # returns the average as described above as a float
    values = []

    for row in grid:
        for col in row:
            values.append(col)

    return sum(values) / len(values)


def main():
    # generating data grid as a nested list
    filename = "data_2.txt"
    grid = create_grid(filename)

    # displaying the grid
    print("This is our grid:")
    display_grid(grid)
    print()

    # filling the gaps
    # zero cells are replaced by mean of neighbors
    new_grid = fill_gaps(grid)

    # displaying new grid
    print("This is our newly calculated grid:")
    display_grid(new_grid)
    print()

    # finding the average and maximum prices
    max = find_max(new_grid)
    avg = find_average(new_grid)

    # display stats
    print("STATS")
    print("Average housing price in this area is: " + str(round(avg)))
    print("Maximum housing price in this area is: " + str(round(max)))


main()
