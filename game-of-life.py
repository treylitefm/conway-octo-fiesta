import copy

def initGrid(width):
    grid = []
    for i in range(width):
        grid.append([])
        for j in range(width):
            grid[i].append([])

    return grid

def printGrid(grid):
    for i in grid:
        row = ''
        for j in i:
            row = row + str(j if j == [] else [j]) + '\t'
        print row + '\n'

def emptyCell(grid, i, j):
    return []

def nonEmptyCell(grid, i, j):
    neighbors = 0
    if i-1 >= 0:
        neighbors = neighbors+1 if grid[i-1][j-1] != [] else neighbors
        neighbors = neighbors+1 if grid[i-1][j] != [] else neighbors
        if j+1 < len(grid):
            neighbors = neighbors+1 if grid[i-1][j+1] != [] else neighbors
    if j-1 >= 0:
        neighbors = neighbors+1 if grid[i][j-1] != [] else neighbors
    if j+1 < len(grid):
        neighbors = neighbors+1 if grid[i][j+1] != [] else neighbors
    if i+1 < len(grid):
        if j-1 >= 0:
            neighbors = neighbors+1 if grid[i+1][j-1] != [] else neighbors
        neighbors = neighbors+1 if grid[i+1][j] != [] else neighbors
        if j+1 < len(grid):
            neighbors = neighbors+1 if grid[i+1][j+1] != [] else neighbors
    print i,j,neighbors
    return 0 if neighbors == 2 or neighbors == 3 else []

grid = initGrid(4)
grid[2][2] = 0
grid[0][0] = 0
grid[1][0] = 0
grid[1][1] = 0
grid[2][0] = 0
grid[3][3] = 0
grid[0][3] = 0
printGrid(grid)
print '-'*30
for i in range(len(grid)):
    gridAtStart = copy.copy(grid)
    for j in range(len(grid)):
        if gridAtStart[i][j] == []:
            grid[i][j] = emptyCell(gridAtStart, i, j)
        else:
            grid[i][j] = nonEmptyCell(gridAtStart, i, j)

printGrid(grid)
