####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *
from random import *

class Flag(object):
    
    def __init__(self):
        self.x0 = choice([190, 410])
        self.x = self.x0
        self.y = 0
        self.width = 50
        self.height = 50
        self.poleOffset = 30
        
        leftCurb = PhotoImage(file = "sprites/flag.gif")
        rightCurb = PhotoImage(file = "sprites/flag2.gif")
        if self.x0 == 190:
            self.image = leftCurb
        else:
            self.image = rightCurb
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)

    def moveX(self):
        if self.x0 == 410:
            ratio = 0.2
            curbX = (2550 + self.y) / 6
            self.x = curbX - ratio * (curbX - 300)
        
        elif self.x0 == 190:
            ratio = 0.2
            curbX = (1050 - self.y) / 6
            self.x = curbX + ratio * (300 - curbX)
    
    def isCollision(self, other):
        other.leftX = other.x - other.width / 2
        other.rightX = other.x + other.width / 2
        other.upY = other.y - other.height / 2
        other.downY = other.y + other.height / 2
        
        self.leftX = self.x - self.width / 2
        self.rightX = self.x + self.width / 2
        self.upY = self.y - self.height / 2
        self.downY = self.y + self.height / 2
        
        if self.rightX >= other.leftX and self.leftX <= other.rightX \
            and self.upY <= other.downY and self.downY >= other.upY:
                return True 
        return False

# class Squirrel(object):
#     
#     def __init__(self):
#         self.x = choice([0, 600])
#         self.y = 0
#         self.speed = -0.75 if self.x == 600 else 0.75
#         self.image = 