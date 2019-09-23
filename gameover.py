####################################
# File contains all of the OOP for the Game Over screen, which is displayed
# after the game ends.

#gameover.py Citation Comment:
#Lines 9-35: Original code
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