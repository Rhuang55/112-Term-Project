####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

import tkinter
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
        return False
        