####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *
from obstacle import *
from track import *

class Buggy(object):

    def __init__(self, x=300, y=300):
        self.name = "Solaris"
        self.x = x
        self.y = y
        self.movespeed = 5
        self.rollspeed = 1
        self.width = 40
        self.height = 80
        self.lives = 1
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.width // 2, self.y - self.height \
            // 2, self.x + self.width // 2, self.y + self.height // 2, \
            fill = "blue")
        canvas.create_rectangle(self.x - self.width // 2, self.y - self.height \
            // 2, self.x + self.width // 2, self.y + self.height // 2, \
            width = 1)
        canvas.create_text(self.x, self.y, fill = "white", text = self.name)
    
    def keymove(self, x, y):
        if x != 0:
            self.x += self.movespeed * x
        if y != 0:
            self.y += self.movespeed * y
    
    def roll(self):
        self.y -= self.rollspeed
    
    def reset(self):
        if self.y < 0:
            self.y = 400

    def isCollision(self, other):
        if isinstance(other, Track):
            if other.leftX1 >= self.x - self.width // 2 or other.rightX0 <= \
                self.x + self.width // 2:
                    return True
        return False