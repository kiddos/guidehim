Guide Him
=========

This is a quick programming game exercise on Markov Decision Processes and Dynamic Programming.

## Requirement

dependencies:

  - numpy (>=1.10.x)
  - gym (>=0.8.0)
  - pygame (>=1.9.3)

type in terminal

  ```shell
  sudo pip install gym numpy pygame
  ```

## Installation

To install to your system:

  ```shell
  git clone https://github.com/kiddos/guidehim.git
  cd guidehim
  sudo python setup.py install
  ```

## Goal

The goal is to guide Stone Lin moving towards the goal. If your command move Stone Lin out of the Screen, game is over and you will need to reset the environemnt to play.

## Properties of Stone Lin

Stone Lin does not always follow the command you gave him, since he is such a dick. He has a probablility of 87.87% to follow your command. For 12.13% chance, he will go the other way. This makes the game a little harder to play.

## Task

Your job is to gave Stone Lin action so that he can get to the goal.

import

  ```python
  from guidehim.guide_him import GuideHim
  ```

initialize environemnt:

  ```python
  env = GuideHim('map/simple.map')
  ```

reset the environemnt:

  ```python
  observation = env.reset()
  ```

give action:

  ```python
  observation, reward, done, _ = env.step(env.action_space.sample())
  ```

render:

  ```python
  env.render()
  ```

sample code:

  ```
  from guidehim.guide_him import GuideHim
  import numpy as np

  def main():
    env = GuideHim('map/simple.map')
    observation = env.reset()
    while True:
      observation, reward, done, _ = env.step(env.action_space.sample())
      env.render()

  if __name__ == '__main__':
    main()
  ```

## Maps

I currently create 3 maps:

  - empty.map
  - simple.map
  - easy.map

You can play around with these.

## Examples

I implement 2 dynamic programming methods:

  - value iteration `value_iteration.py`
  - policy iteration `policy_iteration.py`

I suggest you implement your own first.
