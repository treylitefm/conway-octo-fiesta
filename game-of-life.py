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

def iterate_grid(grid):
    gridAtStart = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if gridAtStart[i][j] == []:
                grid[i][j] = empty_cell(gridAtStart, i, j)
            else:
                grid[i][j] = non_empty_cell(gridAtStart, i, j)

grid = init_grid(70)
grid[30][30] = 0
grid[30][33] = 0
grid[31][30] = 0
grid[31][31] = 0
grid[32][30] = 0
grid[32][32] = 0
grid[33][33] = 0
print_grid(grid)
for i in range(10):
    print '-'*30
    iterate_grid(grid)
    print_grid(grid)

