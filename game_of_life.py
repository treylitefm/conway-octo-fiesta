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

def iterate_grid(grid, foresight=None):
    live = []
    foresight = False if foresight == None or foresight == False else True
    print foresight, 'yoo'

    gridAtStart = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if gridAtStart[i][j] == []:
                grid[i][j] = empty_cell(gridAtStart, i, j)
                if _is_active(grid, i, j):
                    live.append([i,j])
            else:
                grid[i][j] = non_empty_cell(gridAtStart, i, j)
                if _is_active(grid, i, j):
                    live.append([i,j])

    if foresight:
        will_live = []
        for i,j in live:
            n = _count_neighbors(grid, i, j)
            if n == 1 or n == 0 or n >= 4:
                will_live.append(False)
            else:
                will_live.append(True)

    if not foresight:
        return map(lambda p: (p[0],p[1]), live)
    else:
        return map(lambda p,i: (p[0],p[1],i), live, will_live)


def populate(grid, points):
    for i,j in points:
        grid[i][j] = 0
    return grid

def main():
    grid = init_grid(20)
    populate(grid, [(10, 10), (10, 13), (11, 10), (11, 11), (12, 10), (12, 12), (13, 13)])

#    print_grid(grid)
    y1,x1 = zip(*live_cells(grid))
    print list(x1)
    print list(y1)

    for i in range(18):
        print '-'*30
        cells = iterate_grid(grid, foresight=True)
        print cells

        #y1,x1 = zip(*live_cells(grid))
        y1,x1,will_live = zip(*cells)
        print i
        print list(x1)
        print list(y1)
        print list(will_live)
        print_grid(grid)


if __name__ == "__main__":
    main()
