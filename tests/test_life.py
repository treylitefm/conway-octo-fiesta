import sys; sys.path.insert(0,'..')

from game_of_life import populate
from game_of_life import init_grid
from game_of_life import live_cells
from game_of_life import iterate_grid
from game_of_life import count_neighbors

import unittest

class TestLife(unittest.TestCase):
    def setUp(self):
        self.grid = init_grid(4)

    def test_init_grid(self):
        self.assertEquals(self.grid, [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]])

    def test_populate(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])

        self.assertEquals(self.grid, [[0,0,0,0], [0,[],[],[]], [0,[],[],[]], [0,[],[],[]]])

    def test_live_cells(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])
        points = live_cells(self.grid)

        self.assertEquals(points, [(0,0),(0,1),(0,2),(0,3), (1,0),(2,0),(3,0)])

    def test_live_cells_with_foresight(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])
        points = live_cells(self.grid, foresight=True)

        self.assertEquals(points, [(0,0,True),(0,1,True),(0,2,True),(0,3,False), (1,0,True),(2,0,True),(3,0,False)])

    def test_iterate_grid(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])
        new_points = iterate_grid(self.grid)
        points = live_cells(self.grid)

        self.assertNotEquals(points, [(0,0),(0,1),(0,2),(0,3), (1,0),(2,0),(3,0)])
        self.assertEquals(new_points, [(0,0),(0,1),(0,2),(1,0), (1,2),(2,0),(2,1)])

    def test_iterate_grid_with_foresight(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])
        new_points = iterate_grid(self.grid, foresight=True)
        points = live_cells(self.grid, foresight=True)

        self.assertNotEquals(points, [(0,0,True),(0,1,True),(0,2,True),(0,3,False), (1,0,True),(2,0,True),(3,0,False)])
        self.assertEquals(new_points, [(0,0,True),(0,1,False),(0,2,True),(1,0,False), (1,2,True),(2,0,True),(2,1,True)])
    
    def test_count_neighbors(self):
        populate(self.grid, [[0,0],[0,1],[0,2],[0,3], [1,0],[2,0],[3,0]])
        points = live_cells(self.grid)

        expected_results = [2,3,2,1,3,2,1]

        for i in range(7):
            point = count_neighbors(self.grid, points[i][0], points[i][1])
            self.assertEquals(point, expected_results[i])
