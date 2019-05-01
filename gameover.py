####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *

class Gameover(object):
    
    def __init__(self):
        self.x0 = 80
        self.x1 = 530
        self.y0 = 420
        self.y1 = 490
        self.image = PhotoImage(file = "sprites/gameover.gif")
    
    def draw(self, canvas):
        canvas.create_image(300, 300, image = self.image)