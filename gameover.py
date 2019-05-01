####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *

class Gameover(object):
    
    def __init__(self, num):
        
        if num == 0:
            self.x0 = 80
            self.x1 = 530
            self.y0 = 420
            self.y1 = 490
            self.image = PhotoImage(file = "sprites/gameover.gif")
        
        else:
            self.x0 = 80
            self.x1 = 530
            self.y0 = 490
            self.y1 = 560
            
            if num == 1:
                self.image = PhotoImage(file = "sprites/p1win.gif")
            
            if num == 2:
                self.image = PhotoImage(file = "sprites/p2win.gif")
    
    def draw(self, canvas):
        canvas.create_image(300, 300, image = self.image)