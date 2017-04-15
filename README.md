Guide Him
=========

![screen_shot](https://raw.githubusercontent.com/kiddos/guidehim/master/screenshot/screenshot1.png)

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

## Objects

You might see these objects on the map:

- Wall: Stone Lin cannot run through wall
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/wall.png" width="40" height="40"></img>

- Fire: If Stone Lin caught on fire, game over.
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/fire.png" width="40" height="40"></img>

- Pond: If Stone Lin fell into a pond, also game over.
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/water.png" width="40" height="40"></img>

- Poop: It's ok to step on poop. Totally ok.
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/poop.png" width="40" height="40"></img>

- 尻尻: It's not ok to 尻尻 in public.
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/mas.png" width="40" height="40"></img>

- 肛肛: It's also not ok to 肛肛 someone else.
<img src="https://raw.githubusercontent.com/kiddos/guidehim/master/guidehim/images/butt.png" width="40" height="40" style="background: black;"></img>



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
