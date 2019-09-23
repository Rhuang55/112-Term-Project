####################################
# File contains all of the OOP for the obstacles on the track, including the
# potholes and pedestrians. This includes checking for collisions and drawing.

#obstacle.py Citation Comment:
#Lines 9-110: Original code
####################################

from tkinter import *
from random import *
from buggy import *

class Pothole(object):
    
    def __init__(self):
        self.x0 = randint(175, 425)
        self.x = self.x0
        self.y = 0
        self.moveCounter = 0
        
        size15 = PhotoImage(file = "sprites/pothole15.gif")
        size20 = PhotoImage(file = "sprites/pothole20.gif")
        size25 = PhotoImage(file = "sprites/pothole25.gif")
        imageSelect = choice([0, 1, 2])

        if imageSelect == 0:
            self.image = size15
            self.r0 = 15
        elif imageSelect == 1:
            self.image = size20
            self.r0 = 20
        elif imageSelect == 2:
            self.image = size25
            self.r0 = 25
        
        self.r = self.r0
    
    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def isCollision(self, other):
        if other.x > self.x:
            buggyWidth = other.x - other.width / 2
        else:
            buggyWidth = other.x + other.width / 2
        
        if other.y > self.y:
            buggyHeight = other.y - other.height / 2
        else:
            buggyHeight = other.y + other.height / 2
            
        distX = abs(self.x - buggyWidth)
        distY = abs(self.y - buggyHeight)
        
        if distX ** 2 + distY ** 2 <= self.r ** 2:
            return True
            
        if other.x > self.x and other.y >= self.y:
            if other.x - self.x - self.r <= 0:
                return other.y - other.height / 2 <= self.y + self.r
        elif self.x > other.x and other.y >= self.y:
            if self.x - self.r - other.x <=0:
                return other.y - other.height / 2 <= self.y + self.r
    
    def moveX(self):
        if self.x0 > 300:
            ratio = (425 - self.x0) / 125
            curbX = (2550 + self.y) / 6
            self.x = curbX - ratio * (curbX - 300)
        
        elif self.x0 < 300:
            ratio = (self.x0 - 175) / 125
            curbX = (1050 - self.y) / 6
            self.x = curbX + ratio * (300 - curbX)

class Pedestrian(object):
    
    def __init__(self):
        self.x = choice([0, 600])
        self.y = 0
        self.scaleFactor = 10/600
        self.width = 42
        self.height = 72
        self.speed = -1 if self.x == 600 else 1
        
        walkRight = PhotoImage(file = "sprites/pedestrian.gif")
        walkLeft = PhotoImage(file = "sprites/pedestrian2.gif")
        if self.x == 0:
            self.image = walkRight
        else:
            self.image = walkLeft

    def draw(self, canvas):
        canvas.create_image(self.x, self.y, image = self.image)
    
    def isCollision(self, other):
        other.leftX = other.x - other.width / 2
        other.rightX = other.x + other.width / 2
        other.upY = other.y - other.height / 2
        other.downY = other.y + other.height / 2
        
        self.leftX = self.x - self.width / 2 + 2
        self.rightX = self.x + self.width / 2 - 2
        self.upY = self.y - self.height / 2 + 2
        self.downY = self.y + self.height / 2 - 2
        
        if self.rightX >= other.leftX and self.leftX <= other.rightX \
            and self.upY <= other.downY and self.downY >= other.upY:
                return True 
        return False