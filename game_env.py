from vizdoom import DoomGame
import random
import time
import numpy as np
from gym import Env
from gym.spaces import Discret, Box
import cv2

class Game_Env(Env):
    def __init__(self):
        self.game = DoomGame()
        self.game.load_config("github/ViZDoom/scenarios/basic.cfg")
        self.game.init()

        self.observation_space = Box(low=0,high=255,shape=(3, 240, 320), dtype= np.uint8)
        self.action_space = Discret(3)


    def step(self, action):
        pass

    def close():
        pass

    def render():
        pass
    def grayscale():
        pass

    def reset():
        pass