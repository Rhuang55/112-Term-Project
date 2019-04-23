####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *
from obstacle import *
from track import *
from math import *

class Buggy(object):

    def __init__(self, x=300, y=500):
        self.name = "Solaris"
        self.x = x
        self.y = y
        self.rollspeed = 0.25
        self.angle = pi / 2
        self.width = 55
        self.height = 110
        self.lives = 3
        self.image = PhotoImage(file = "sprites/solaris.gif")
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def brake(self):
        if self.rollspeed >= -0.4:
            self.rollspeed -= 0.1
    
    def accelerate(self):
        self.rollspeed += 0.1
        
    def turnLeft(self):
        angle = pi / 12
        if self.angle < pi:
            if self.rollspeed >= 0:
                self.angle += angle
            else:
                self.angle -= angle
    
    def turnRight(self):
        angle = pi / 12
        if self.angle > 0:
            if self.rollspeed >= 0:
                self.angle -= angle
            else:
                self.angle += angle
    
    def roll(self):
        self.y -= self.rollspeed
        self.x += self.rollspeed * cos(self.angle)

    def isCollision(self, other):
        if isinstance(other, Track):
            if other.leftX1 >= self.x - self.width // 2 or other.rightX0 <= \
                self.x + self.width // 2:
                    return True
        return False