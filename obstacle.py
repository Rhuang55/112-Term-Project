####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

import tkinter
from random import *
from buggy import *

class Pothole(object):
    
    def __init__(self):
        self.x = randint(200, 400)
        self.y = 0
        self.r = 20
        
        size15 = PhotoImage(file = "sprites/pothole15.gif")
        size20 = PhotoImage(file = "sprites/pothole20.gif")
        size25 = PhotoImage(file = "sprites/pothole25.gif")
        potholes = [size20, size15, size25]
        self.image = choice(potholes)
    
    
    def draw(self, canvas, x, y):
        canvas.create_image(x, y, image = self.image)
    
    def generate(self):
        return [self.x, self.y]

class Pedestrian(object):
    
    def __init__(self):
        self.x = choice([0, 600])
        self.y = 0
        self.scaleFactor = 10/600
        self.width = 20
        self.height = 60
        self.speed = -1 if self.x == 600 else 1
    
    def draw(canvas, x, y):
        canvas.create_rectangle(x, y, x + 20, y + 60)
    
    def generate(self):
        return [self.x, self.y, self.speed]