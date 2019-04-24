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
        
        size15 = PhotoImage(file = "sprites/pothole15.gif")
        size20 = PhotoImage(file = "sprites/pothole20.gif")
        size25 = PhotoImage(file = "sprites/pothole25.gif")
        imageSelect = choice([0, 1, 2])

        if imageSelect == 0:
            self.image = size15
            self.r = 15
        elif imageSelect == 1:
            self.image = size20
            self.r = 20
        elif imageSelect == 2:
            self.image = size25
            self.r = 25
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def isCollision(self, other):
        if other.x > self.x:
            buggyWidth = other.x - other.width / 2
        else:
            buggyWidth = other.x + other.width / 2
        
        if other.y > self.y:
            buggyHeight = other.y - other.height / 2 - 5
        else:
            buggyHeight = other.y + other.height / 2 + 5
            
        distX = abs(self.x - buggyWidth)
        distY = abs(self.y - buggyHeight)
        
        return distX ** 2 + distY ** 2 <= self.r ** 2 - (self.r / 3)

class Pedestrian(object):
    
    def __init__(self):
        self.x = choice([0, 600])
        self.y = 0
        self.scaleFactor = 10/600
        self.width = 42
        self.height = 72
        self.speed = -1 if self.x == 600 else 1
        self.image = PhotoImage(file = "sprites/pedestrian.gif")
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def isCollision(self, other):
        other.leftX = other.x - other.width / 2
        other.rightX = other.x + other.width / 2
        other.upY = other.y - other.height / 2
        other.downY = other.y + other.height / 2
        
        if other.leftX <= self.x <= other.rightX and \
            other.upY <= self.y <= other.downY:
                return True
        return False