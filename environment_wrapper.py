from collections import deque
import gym
import numpy as np
import random 

class EnvironmentWrapper(gym.Wrapper):
    def __init__(self, env, k):
        gym.Wrapper.__init__(self, env)
        self.k = k
        self.x = env
        self.frames = deque([], maxlen=k)
        shp = env.observation_space.shape
        self.observation_space_n = env.observation_space.n
        self.observation_space = \
            gym.spaces.Box(low=0, high=255, shape=((k,) + shp), dtype=env.observation_space.dtype)

    def step(self, action):
        obs, reward, done, err, info = self.env.step(action)
        return (np.array(obs), reward, done, info)

    def _get_ob(self):
        return np.array(self.frames, dtype=object)

class ObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def observation(self, obs):
        # Normalise observation by 255
        return obs

class RewardWrapper(gym.RewardWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def reward(self, reward):
        # Clip reward between 0 to 1
        return np.clip(reward, 0, 1)

    
class ActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def action(self, action):
        if action == 0:
            return random.choice([2,3])
        else:
            return action
