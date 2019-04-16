####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

import tkinter
from random import randint
from buggy import *

class Pothole(object):
    
    def __init__(self):
        self.x = randint(100, 500)
        self.y = randint(0, 400)
        self.r = randint(5, 30)
    
    def draw(canvas, x, y, r):
        canvas.create_oval(x - r, y - r, x + r, y + r, fill = "black")
        canvas.create_rectangle(x - r, y - r, x + r, y + r, width = 1)
    
    def generate(self):
        return (self.x, self.y, self.r)