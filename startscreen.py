####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *

class Startscreen(object):
    
    def __init__(self):
        self.p1x0 = 100
        self.p1x1 = 500
        self.p1y0 = 370
        self.p1y1 = 440
        self.image = PhotoImage(file = "sprites/startscreen.gif")
    
    def draw(self, canvas):
        canvas.create_image(300, 300, image = self.image)