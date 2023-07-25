import os
import imageio
import numpy as np
from PIL import Image
import PIL.ImageDraw as ImageDraw
import matplotlib.pyplot as plt
import math

import torch
import torch.nn.functional as F
import torch.nn as nn
import random
from torchvision import transforms
from fileIO import FileIO


# def fix_state(states):
#     state_tup = []
#     for state in list(states):
#         if isinstance(state, tuple): state_tup.append(state[0])
#         else: state_tup.append(state)
#     return tuple(state_tup)
    
       
def label_with_episode_number(frame, episode_num):
    im = Image.fromarray(frame)

    drawer = ImageDraw.Draw(im)

    if np.mean(im) < 128:
        text_color = (255,255,255)
    else:
        text_color = (0,0,0)
    drawer.text((im.size[0]/20,im.size[1]/18), f'Episode: {episode_num+1}', fill=text_color)

    return im


def save_random_agent_gif(env, frames, name):
    print('------------ saving gif file -------------')
    env.close()
    imageio.mimwrite(os.path.join('./', name+'.gif'), frames, duration=20)
    print('------------ successfully saved gif file -------------')
    
# used to prepare a state to be used by a cnn network
def preprocess_frame(frame):
    frame = frame[34:194, :, :]
    # frame = np.transpose(frame, (2, 0, 1))  # Transpose dimensions to (3, 210, 160)
    frame = frame.mean(axis=2).astype('uint8')
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    return frame

def transform(frame, add_batch=True):
    """transform the state (210, 160, 3) to tensor (1, 3, 210, 160) or (3, 210, 160)"""
    transformer = transforms.Compose([
        transforms.ToPILImage(),  # Convert to PIL Image
        transforms.Resize((160, 160)),  # Resize the image
        transforms.ToTensor()  # Convert to a PyTorch tensor
    ])
    return transformer(frame).unsqueeze(0) if add_batch else transformer(frame)


class ReplayBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def push(self, experience):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = experience
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)
    
class QTable:
    def __init__(self, *args) -> None:
        self.grid = np.zeros(tuple(args))
        
    
        

def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
    

def write_history(path, data):
    history = FileIO(path)
    history.append(data)
    history.close()   

def get_last_history(path):
    history = FileIO(path, 'r')
    last_line =  history.read_last_line().split(',')[0]
    history.close()
    return int(last_line)

def compute_reward(reward, done):
    trad = 0
    nontrad = 0
    
    # clip traditional reward to 0 or 5
    if (reward > 0):
        trad = 1
    
    # give a non-traditional reward for staying in the game
    if (not done):
        nontrad = 0.1
    else:
        nontrad = -0.1
        
    return trad, nontrad

def decimal2(x): return math.floor(x*100)/100
        
    
