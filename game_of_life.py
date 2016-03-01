import copy

'''
Inspired by: http://www.bitstorm.org/gameoflife/
'''

def init_grid(width):
    grid = []
    for i in range(width):
        grid.append([])
        for j in range(width):
            grid[i].append([])

    return grid

def print_grid(grid):
    for i in grid:
        row = ''
        for j in i:
            row = row + str(j if j == [] else [j]) + '\t'
        print row + '\n'

def empty_cell(grid, i, j):
    neighbors = _count_neighbors(grid, i, j)
    return 0 if neighbors == 3 else []

def non_empty_cell(grid, i, j):
    neighbors = _count_neighbors(grid, i, j)
    return 0 if neighbors == 2 or neighbors == 3 else []

def _count_neighbors(grid, i, j):
    neighbors = 0
    if i-1 >= 0:
        if j-1 >= 0:
            neighbors = neighbors+1 if grid[i-1][j-1] != [] else neighbors #top-left
        neighbors = neighbors+1 if grid[i-1][j] != [] else neighbors #top-center

        if j+1 < len(grid):
            neighbors = neighbors+1 if grid[i-1][j+1] != [] else neighbors #top=right

    if j-1 >= 0:
        neighbors = neighbors+1 if grid[i][j-1] != [] else neighbors #center-left

    if j+1 < len(grid):
        neighbors = neighbors+1 if grid[i][j+1] != [] else neighbors #center-right

    if i+1 < len(grid):
        if j-1 >= 0:
            neighbors = neighbors+1 if grid[i+1][j-1] != [] else neighbors #lower-left
        neighbors = neighbors+1 if grid[i+1][j] != [] else neighbors #lower-center

        if j+1 < len(grid):
            neighbors = neighbors+1 if grid[i+1][j+1] != [] else neighbors #lower-right

    return neighbors

def _is_active(grid, i, j):
    return grid[i][j] == 0

def live_cells(grid):
    live = []

    for i in range(len(grid)):
        for j in range(len(grid)):
            if _is_active(grid, i, j):
                live.append((i,j))
    return live

def iterate_grid(grid):
    live = []

    gridAtStart = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if gridAtStart[i][j] == []:
                grid[i][j] = empty_cell(gridAtStart, i, j)
                if _is_active(grid, i, j):
                    live.append((i,j))
            else:
                grid[i][j] = non_empty_cell(gridAtStart, i, j)
                if _is_active(grid, i, j):
                    live.append((i,j))
    return live

def populate(grid, points):
    for i,j in points:
        grid[i][j] = 0
    return grid

def main():
    grid = init_grid(20)
    populate(grid, [(10, 10), (10, 13), (11, 10), (11, 11), (12, 10), (12, 12), (13, 13)])

    print_grid(grid)
    for i in range(10):
        print '-'*30
        iterate_grid(grid)
        print_grid(grid)


if __name__ == "__main__":
    main()
