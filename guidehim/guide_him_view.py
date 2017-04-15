import pygame
import os
import sys
import signal
import logging
import time
import threading

from map import Map
from g8guy import G8Guy

GRID_SIZE = 80
PADDING = 10
DELTA = GRID_SIZE / 10
IMAGE_DIR = 'images'
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class GuideHimView(object):
  def __init__(self, path, g8guy=None):
    logging.basicConfig()
    self.logger = logging.getLogger(name='guide_him')
    self.logger.setLevel(logging.INFO)
    signal.signal(signal.SIGINT, lambda sig, frame: self.close())
    self.m = Map(path)
    if g8guy is None:
      self.guy = G8Guy(*self.m.get_start())
    else: self.guy = g8guy
    self.gx = self.guy.x * GRID_SIZE + PADDING
    self.gy = self.guy.y * GRID_SIZE + PADDING
    self.dx = self.dy = 0

  def _load_image(self, name):
    path = os.path.join(CURRENT_DIR, IMAGE_DIR, name)
    self.logger.info('loading %s...' % (path))
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (GRID_SIZE, GRID_SIZE))
    return img

  def init(self):
    self.logger.info('init pygame screen')
    pygame.init()
    self.size = [PADDING * 2 + GRID_SIZE * self.m.cols,
        PADDING * 2 + GRID_SIZE * self.m.rows]
    self.screen = pygame.display.set_mode(self.size)
    # images
    self.wall = self._load_image('wall.png')
    self.fire = self._load_image('fire.png')
    self.water = self._load_image('water.png')
    self.poop = self._load_image('poop.png')
    self.mast = self._load_image('mas.png')
    self.butt = self._load_image('butt.png')
    self.g8guy = self._load_image('g8guy.png')
    self.goal = self._load_image('goal.png')

  def draw(self):
    self.screen.fill((0, 0, 0))
    color = (100, 100, 100)
    for i in range(self.m.cols + 1):
      pygame.draw.line(self.screen, color,
          [PADDING + i * GRID_SIZE, PADDING],
          [PADDING + i * GRID_SIZE, self.size[0] - PADDING], 2)
      pygame.draw.line(self.screen, color,
          [PADDING, PADDING + i * GRID_SIZE],
          [self.size[1] - PADDING, PADDING + i * GRID_SIZE], 2)
    # grid
    for i in range(self.m.rows):
      for j in range(self.m.cols):
        if self.m.in_wall(j, i):
          self.screen.blit(self.wall,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.on_fire(j, i):
          self.screen.blit(self.fire,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.in_water(j, i):
          self.screen.blit(self.water,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.on_poop(j, i):
          self.screen.blit(self.poop,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.do_masturbating(j, i):
          self.screen.blit(self.mast,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.do_anal(j, i):
          self.screen.blit(self.butt,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
        elif self.m.reached_goal(j, i):
          self.screen.blit(self.goal,
              [j * GRID_SIZE + PADDING, i * GRID_SIZE + PADDING])
    # draw g8guy
    self.screen.blit(self.g8guy, [self.gx, self.gy])
    pygame.display.flip()

  def update(self):
    if self.dx != 0:
      d = -DELTA if self.dx > 0 else 0
      self.gx -= d
      self.dx += d
    if self.dy != 0:
      d = -DELTA if self.dy > 0 else 0
      self.gy -= d
      self.dy += d

  def check_close(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.close()

  def close(self):
    self.logger.info('closing...')
    sys.exit()

  def update_guy_pose(self, x, y):
    self.dx += (x - self.guy.x) * GRID_SIZE
    self.dy += (y - self.guy.y) * GRID_SIZE
    self.guy = G8Guy(x, y)

  def loop(self):
    while True:
      self.check_close()
      self.draw()
      self.update()

  def start_in_background(self):
    self.init()
    task = threading.Thread(target=self.loop)
    task.start()


if __name__ == '__main__':
  current_dir = os.path.dirname(os.path.realpath(__file__))
  view = GuideHimView(os.path.join(current_dir, '..', 'map', 'simple.map'))
  view.start_in_background()
  while True:
    view.update_guy_pose(1, 0)
    time.sleep(1)
