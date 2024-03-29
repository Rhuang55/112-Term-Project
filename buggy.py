####################################
# File contains all of the OOP for the Buggy object, which the user drives
# around the course

#buggy.py Citation Comment:
#Lines 9-47: Original code
####################################

from tkinter import *
from obstacle import *
from track import *
from math import *

class Buggy(object):

    def __init__(self, image, x=300, y=500):
        self.x = x
        self.y = y
        self.rollspeed = 0.5
        self.xspeed = 0
        self.width = 55
        self.height = 100
        self.lives = 3
        self.image = image
        self.immune = False
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def brake(self):
        if self.rollspeed >= -0.4:
            self.rollspeed -= 0.1
    
    def accelerate(self):
        self.rollspeed += 0.1
        
    def turnLeft(self):
        if self.xspeed > -0.5:
            self.xspeed -= 0.1
    
    def turnRight(self):
        if self.xspeed < 0.5:
            self.xspeed += 0.1
    
    def roll(self):
        self.y -= (self.rollspeed - 0.5)
        self.x += self.xspeed * (self.rollspeed + 0.5)