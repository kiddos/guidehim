import os
import logging
import unittest


class Map(object):
  def __init__(self, path):
    self.logger = logging.getLogger(name='guide-him')
    if os.path.isfile(path):
      with open(path, 'r') as f:
        content = f.read()
      self.grid = [[int(i) for i in line.strip().split(' ')]
          for line in content.strip().split('\n')]
      self.rows = len(self.grid)
      self.cols = len(self.grid[0])
    else:
      self.logger.error('%s not found' % (path))

  def in_range(self, x, y):
    return x >= 0 and x < self.cols and y >=0 and y < self.rows

  def on_nothing(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] in [0, 8]

  def in_wall(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 1

  def on_fire(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 2

  def in_water(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 3

  def on_poop(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 4

  def do_masturbating(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 5

  def do_anal(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 6

  def reached_goal(self, x, y):
    return self.in_range(x, y) and self.grid[y][x] == 9

  def get_start(self):
    for i in range(self.rows):
      for j in range(self.rows):
        if self.grid[i][j] == 8:
          return (i, j)
    return None

  def get_end(self):
    for i in range(self.rows):
      for j in range(self.rows):
        if self.grid[i][j] == 9:
          return (i, j)


  def output_pose(self, x, y):
    state = ''
    for i in range(self.rows):
      for j in range(self.cols):
        if i == y and x == j:
          state += '@ '
        elif self.grid[i][j] == 0:
          state += '  '
        elif self.grid[i][j] in [1, 2, 3, 4, 5, 6]:
          h = i > 0 and i < self.rows - 1
          v = j > 0 and j < self.cols - 1
          if h and v:
            state += '+ '
          elif h:
            state += '| '
          else:
            state += '- '
        elif self.grid[i][j] == 8:
          state += '^ '
        elif self.grid[i][j] == 9:
          state += '$ '
      state += '\n'
    return state

  def __str__(self):
    return self.output_pose(-1, -1)


class TestMap(unittest.TestCase):
  def test_map(self):
    m = Map('map/simple.map')
    self.assertEqual(m.grid,
        [[8, 0, 0, 0], [0, 0, 0, 0],
         [0, 0, 0, 0], [0, 0, 0, 9]])

  def test_in_range(self):
    m = Map('map/simple.map')
    self.assertTrue(m.in_range(0, 0))
    self.assertTrue(m.in_range(3, 3))
    self.assertTrue(m.in_range(0, 3))
    self.assertTrue(m.in_range(3, 0))
    self.assertFalse(m.in_range(-1, -1))
    self.assertFalse(m.in_range(0, -1))
    self.assertFalse(m.in_range(-1, 0))
    self.assertFalse(m.in_range(4, 4))
    self.assertFalse(m.in_range(4, 0))
    self.assertFalse(m.in_range(0, 4))

  def test_get_start(self):
    m = Map('map/simple.map')
    self.assertEqual(m.get_start(), (0, 0))

  def test_get_end(self):
    m = Map('map/simple.map')
    self.assertEqual(m.get_end(), (3, 3))


if __name__ == '__main__':
  unittest.main()
