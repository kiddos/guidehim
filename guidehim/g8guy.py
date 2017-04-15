import os
import random
import unittest


class G8Guy(object):
  def __init__(self, ix, iy):
    self.x = ix
    self.y = iy

  def move_x(self, dx):
    chance = random.uniform(0, 1)
    if chance < 0.8787:
      self.x += dx
    else:
      chance = random.uniform(0, 1)
      if chance > 0.5:
        self.y += dx
      else:
        self.y -= dx


  def move_y(self, dy):
    chance = random.uniform(0, 1)
    if chance < 0.8787:
      self.y += dy
    else:
      chance = random.uniform(0, 1)
      if chance > 0.5:
        self.x += dy
      else:
        self.x -= dy


class TestPerson(unittest.TestCase):
  def test_move_x(self):
    correct = 0
    for i in range(100):
      p = G8Guy(0, 0)
      p.move_x(1)
      if p.y == 0 and p.x == 1:
        correct += 1
    self.assertTrue(correct > 83)

  def test_move_y(self):
    correct = 0
    for i in range(100):
      p = G8Guy(0, 0)
      p.move_y(1)
      if p.x == 0 and p.y == 1:
        correct += 1
    self.assertTrue(correct > 83)


if __name__ == '__main__':
  unittest.main()
