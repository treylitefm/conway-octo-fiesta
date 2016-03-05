from game_of_life import populate
from game_of_life import init_grid
from game_of_life import live_cells
from game_of_life import iterate_grid

import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import json

def main():
    with open('templates.json', 'r') as json_data:
        templates = json.load(json_data)

    fig = plt.figure()
    
    grid = init_grid(20); populate(grid, templates['sample0'])

    points = live_cells(grid, foresight=True)
    y1,x1,will_live = zip(*points)
    c1 = ['g' if life == True else 'r' for life in will_live]
    scat = plt.scatter(x1, y1, c=c1, s=100)
    
    def init():
        time.sleep(5)
        points = live_cells(grid, foresight=True)
        y1,x1,will_live = zip(*points)
        c1 = ['g' if life == True else 'r' for life in will_live]
        scat = plt.scatter(x1, y1, c=c1, s=100)
        print list(x1)
        print list(y1)
        print list(c1)
        print '0'*20
        return scat,

    anim = animation.FuncAnimation(fig, update_plot, init_func=init, interval=1500, fargs=(scat, grid), blit=False)

    #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.axis([0,20,0,20])
    plt.show()


def update_plot(i, scat, grid):
    plt.cla()

    points = live_cells(grid, foresight=True) if i == 0 else iterate_grid(grid, foresight=True)
    y1,x1,will_live = zip(*points) if points != [] else ((),(),())
    c1 = ['g' if life == True else 'r' for life in will_live]

    
    print 'i',i
    print list(x1)
    print list(y1)
    print list(c1)
    print '-'*20

    scat = plt.scatter(x1, y1, c=c1, s=100)
    plt.axis([0,20,0,20])
    return scat,


if __name__ == "__main__":
    main()
