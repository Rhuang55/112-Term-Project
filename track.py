####################################
# File contains all of the OOP for the Track and Indicator objects. The Track
# object is responsible for drawing the track and the yellow lines and
# detecting curb collisions. The indicator object is responsible for creating
# and drawing life/powerup indicators on the screen.

#track.py Citation Comment:
#Lines 11-112: Original code
####################################

from tkinter import *
from buggy import *

class Track(object):
    
    def __init__(self):
        self.leftX0 = 150
        self.leftX1 = 175
        self.rightX0 = 425
        self.rightX1 = 450
        self.farOff = 100
        self.closeOff = 100
        
        #yellow line parameters
        self.topLeft = 300 - 5
        self.topRight = 300 + 5
        self.bottomRight = 300 + 5
        self.bottomLeft = 300 - 5
    
    def draw(self, canvas):
        #road
        canvas.create_polygon(self.leftX1, 0, self.rightX0, 0, self.rightX0 + \
            self.farOff, 600, self.leftX1 - self.farOff, 600, \
            fill = "dark gray")
        #left curb
        canvas.create_polygon(self.leftX0, 0, self.leftX1, 0, self.leftX1 - \
            self.farOff, 600, self.leftX0 - self.closeOff, 600, \
            fill = "light gray")
        #right curb
        canvas.create_polygon(self.rightX0, 0, self.rightX1, 0, self.rightX1 + \
            self.closeOff, 600, self.rightX0 + self.farOff, 600, \
            fill = "light gray")
    
    def makeYellowLines(self, number):
        return [self.topLeft, self.topRight, self.bottomRight, \
            self.bottomLeft, number]
    
    def drawYellowLines(self, canvas, line):
        scaleFactor = 10/600
        topLeft = line[0] - scaleFactor * line[4]
        topRight = line[1] + scaleFactor * line[4]
        bottomRight = line[2] + scaleFactor * (line[4] + 60)
        bottomLeft = line[3] - scaleFactor * (line[4] + 60)
        
        canvas.create_polygon(topLeft, line[4], topRight, line[4], \
            bottomRight, line[4] + 60, bottomLeft, line[4] + 60, \
            fill = "yellow")
    
    def isCollision(self, other):
        leftCurb = (1050 - other.y) / 6
        rightCurb = (2550 + other.y) / 6
        if leftCurb >= other.x - other.width / 2:
            return True
        if rightCurb <= other.x + other.width / 2:
            return True
        if not (0 <= other.y + other.height / 2):
            return True
        if not (other.y - other.height / 2 <= 600):
            return True
        return False

class Indicators(object):
    
    def __init__(self, num):
        self.player = num
        
        if self.player == 1:
            self.heartX = 567
            self.heartY = 60
            self.heartImage = PhotoImage(file = "sprites/heart.gif")
            
            self.potholeX = 550
            self.potholeY = 15
            self.potholeImage = PhotoImage(file = "sprites/potholeIndic.gif")
            
            self.pedestX = 585
            self.pedestY = 15
            self.pedestImage = PhotoImage(file = "sprites/pedestIndic.gif")
        
        elif self.player == 2:
            self.heartX = 33
            self.heartY = 60
            self.heartImage = PhotoImage(file = "sprites/heart.gif")
            
            self.potholeX = 16
            self.potholeY = 15
            self.potholeImage = PhotoImage(file = "sprites/potholeIndic.gif")
            
            self.pedestX = 48
            self.pedestY = 15
            self.pedestImage = PhotoImage(file = "sprites/pedestIndic.gif")
    
    def drawHeart(self, canvas):
        canvas.create_image(self.heartX, self.heartY, image = self.heartImage)
    
    def drawPothole(self, canvas):
        canvas.create_image(self.potholeX, self.potholeY, \
            image = self.potholeImage)
    
    def drawPedest(self, canvas):
        canvas.create_image(self.pedestX, self.pedestY, \
            image = self.pedestImage)