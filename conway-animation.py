from game_of_life import populate
from game_of_life import init_grid
from game_of_life import live_cells
from game_of_life import iterate_grid

import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def main():
    numframes = 100

    fig = plt.figure()
    scat = plt.scatter([], [], s=100)

    
    grid = init_grid(20); populate(grid, [(10, 10), (10, 13), (11, 10), (11, 11), (12, 10), (12, 12), (13, 13)])
    points = live_cells(grid)
    x1,y1 = zip(*points)
    c1 = np.random.random_integers(0, 10, len(points))
    print list(x1)
    print list(y1)
    print list(c1)
    print '-'*20



    anim = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes), fargs=(scat, grid), blit=False)

    #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.axis([0,20,0,20])
    plt.show()



def update_plot(i, scat, grid):
    plt.cla()
    time.sleep(1)
    '''numframes = 100
    numpoints = 10
    #x, y, c = np.random.random((3, numpoints))
    x, y, c = np.random.random_integers(0,40,(3, numpoints))
    print '*'*20
    print 'x',x
    print 'y',y
    print 'c',c
    print '*'*20
    print '-'*20
    '''
    #import game_of_life; grid = game_of_life.init_grid(10); game_of_life.populate(grid, [(1,1), (2,2), (3,3), (4,4), (1,0), (2,4), (5,5), (2,7), (7,5), (4,5)])
    points = iterate_grid(grid)
    x1,y1 = zip(*points)
    c1 = np.random.random_integers(0, 10, len(points))
    print list(x1)
    print list(y1)
    print list(c1)
    print '-'*20

    scat = plt.scatter(x1, y1, c=c1, s=100)
    plt.axis([0,20,0,20])
    return scat,

main()
