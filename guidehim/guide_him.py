import os
import logging
import unittest
import numpy as np
from gym import Env, spaces
import random

from map import Map
from g8guy import G8Guy
from guide_him_view import GuideHimView


NAME = 'Stone Lin'


class GuideHim(Env):
  metadata = {'render.modes': ['ansi', 'rgb_array', 'human']}

  def __init__(self, path):
    self.path = path
    self.logger = logging.getLogger('guide-him')
    self.logger.setLevel(logging.INFO)
    self._reset()
    self.spec = None
    self.action_space = spaces.Tuple((spaces.Discrete(2), spaces.Discrete(2)))
    self.observation_space = spaces.Box(low=0, high=9,
        shape=(self.m.rows, self.m.cols))
    self.view = None

  def _seed(self, seed=None):
    random.seed(seed)

  def get_state(self):
    state = np.array(self.m.grid, dtype=np.uint8)
    state[state == 8] = 0
    if self.m.in_range(self.guy.x, self.guy.y):
      state[self.guy.y][self.guy.x] = 8
    return state

  def _step(self, action):
    assert len(action) == 2
    if action[0] != 0:
      self.guy.move_y(action[0])
    else:
      self.guy.move_x(action[1])

    reward = 0
    done = False
    x = self.guy.x
    y = self.guy.y
    if not self.m.in_range(x, y):
      self.logger.info(NAME + ' ran away.')
      reward = -1
      done = True
    elif self.m.on_nothing(x, y):
      self.logger.info(NAME + ' is kinda safe.')
      reward = 1
    elif self.m.in_wall(x, y):
      self.logger.info(NAME + ' ran into a wall.')
      reward = -1
      done = True
    elif self.m.on_fire(x, y):
      self.logger.info(NAME + ' caught on fire.')
      reward = -1
      done = True
    elif self.m.on_poop(x, y):
      self.logger.info(NAME + ' step on poop.')
      reward = 1
    elif self.m.do_masturbating(x, y):
      self.logger.info(NAME + ' is probably masturbating.')
      reward = 1
    elif self.m.do_anal(x, y):
      self.logger.info(NAME + '\'s anal is getting hurt!!')
      reward = -1
      done = True
    elif self.m.reached_goal(self.guy.x, self.guy.y):
      self.logger.info(NAME + ' reach the goal.')
      reward = 10
      done = True
    return self.get_state(), reward, done, {}

  def _reset(self):
    self.m = Map(self.path)
    self.guy = G8Guy(*self.m.get_start())
    return self.get_state()

  def _render(self, mode='human', close=False):
    if not close:
      if mode == 'rgb_array':
        return np.array(self.m.grid, dtype=np.uint8)
      elif mode is 'human':
        if self.view is None:
          self.view = GuideHimView(self.path, self.guy)
          self.view.start_in_background()
        if self.view is not None:
          self.view.update_guy_pose(self.guy.x, self.guy.y)
      else:
        self.logger.info('\n' + str(self.m.output_pose(self.guy.x, self.guy.y)))

  def _close(self):
    pass


class TestGuideHim(unittest.TestCase):
  def test_init(self):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    gh = GuideHim(os.path.join(current_dir, '..', 'map', 'simple.map'))
    self.assertTrue(gh.guy.x == 0)
    self.assertTrue(gh.guy.y == 0)


if __name__ == '__main__':
  unittest.main()
