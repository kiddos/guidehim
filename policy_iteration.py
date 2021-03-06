from __future__ import print_function
from guidehim.guide_him import GuideHim
import numpy as np
import time

# up, down, left, right
ACTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
TRANSITION_PROB = [0.8787, 0.06065, 0.06065]
DISCOUNT_FACTOR = 0.99


def reward_function(observation, x, y):
  state = observation[y][x]
  if state in [0, 4, 8]:
    return 1
  elif state in [1, 2, 3, 5, 6]:
    return -30
  elif state == 9:
    return 30


def policy_iteration(state_shape, observation, max_epoch=600):
  policy = np.zeros(state_shape, dtype=np.uint8)
  values = np.zeros(state_shape)
  for epoch in range(max_epoch):
    for i in range(state_shape[0]):
      for j in range(state_shape[1]):
        # update value function
        r = reward_function(observation, j, i)
        p = policy[i][j]
        v = 0
        for k, d in enumerate([0, -1, 1]):
          action = ACTIONS[(p + d) % (len(ACTIONS))]
          y = i + action[0]
          x = j + action[1]
          if y >= 0 and y < state_shape[0] and x >= 0 and x < state_shape[1]:
            v += r + DISCOUNT_FACTOR * TRANSITION_PROB[k] * values[y][x]
        values[i][j] = v
        # update policy
        vs = []
        for p in range(len(ACTIONS)):
          v = 0
          for k, d in enumerate([0, -1, 1]):
            action = ACTIONS[(p + d) % (len(ACTIONS))]
            y = i + action[0]
            x = j + action[1]
            if y >= 0 and y < state_shape[0] and x >= 0 and x < state_shape[1]:
              v += r + DISCOUNT_FACTOR * TRANSITION_PROB[k] * values[y][x]
          vs.append(v)
        policy[i][j] = np.argmax(np.array(vs))
  return policy, values


def main():
  env = GuideHim('map/simple.map')
  env.seed()
  observation = env.reset()
  print(observation)
  policy, values = policy_iteration(env.observation_space.shape, observation)
  print(policy)
  while True:
    p = ACTIONS[policy[observation == 8][0]]
    observation, reward, done, _ = env.step(p)
    env.render()
    time.sleep(0.5)
    if done:
      break


if __name__ == '__main__':
  main()
