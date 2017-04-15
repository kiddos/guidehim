from __future__ import print_function
from guidehim.guide_him import GuideHim
import numpy as np


def main():
  env = GuideHim('map/simple.map')
  env.seed()
  env.reset()
  while True:
    observation, reward, done, _ = env.step(env.action_space.sample())
    env.render()


if __name__ == '__main__':
  main()
