####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

import tkinter
from buggy import *

class Track(object):
    
    def __init__(self):
        self.leftX0 = 75
        self.leftX1 = 100
        self.rightX0 = 500
        self.rightX1 = 525
    
    def draw(self, canvas):
        canvas.create_rectangle(self.leftX1, 0, self.rightX0, 400, \
            fill = "dark gray")
        canvas.create_rectangle(self.leftX0, 0, self.leftX1, 400, \
            fill = "light gray")
        canvas.create_rectangle(self.rightX0, 0, self.rightX1, 400, \
            fill = "light gray")