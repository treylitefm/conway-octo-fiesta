from game_of_life import populate
from game_of_life import init_grid
from game_of_life import live_cells
from game_of_life import iterate_grid

import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import json
import sys

def main():
    with open('templates.json', 'r') as json_data:
        templates = json.load(json_data)

    print 'Choose a template:'
    for key in templates:
        print '-',key

    print '\n'
    response = raw_input()

    if response not in templates:
        print 'Not a valid option'
        sys.exit(0)
        


    valid_speeds = ['f','fast','m','med','medium','s','slow']
    
    while True:
        print 'How fast? [f]ast/[m]ed/[s]low'
        speed = raw_input()

        if speed in valid_speeds:
            break

    speed = speed.lower()

    if speed == 'f' or speed == 'fast':
        speed = 100
    elif speed == 'm' or speed == 'med' or speed == 'medium':
        speed = 800
    else:
        speed = 1500


    fig = plt.figure()
    
    grid = init_grid(50); populate(grid, templates[response])

    points = live_cells(grid, foresight=True)
    x1,y1,will_live = zip(*points)
    c1 = ['g' if life == True else 'r' for life in will_live]
    scat = plt.scatter(x1, y1, c=c1, s=30)
    
    def init():
        time.sleep(5)
        points = live_cells(grid, foresight=True)
        x1,y1,will_live = zip(*points)
        c1 = ['g' if life == True else 'r' for life in will_live]
        scat = plt.scatter(x1, y1, c=c1, s=30)
        #print list(x1)
        #print list(y1)
        #print list(c1)
        #print '0'*20
        return scat,

    anim = animation.FuncAnimation(fig, update_plot, init_func=init, interval=speed, fargs=(scat, grid), blit=False)

    #anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.axis([0,50,0,50])
    plt.show()


def update_plot(i, scat, grid):
    plt.cla()

    points = live_cells(grid, foresight=True) if i == 0 else iterate_grid(grid, foresight=True)
    x1,y1,will_live = zip(*points) if points != [] else ((),(),())
    c1 = ['g' if life == True else 'r' for life in will_live]

    
    #print 'i',i
    #print list(x1)
    #print list(y1)
    #print list(c1)
    #print '-'*20

    scat = plt.scatter(x1, y1, c=c1, s=30)
    plt.axis([0,50,0,50])
    return scat,


if __name__ == "__main__":
    main()
