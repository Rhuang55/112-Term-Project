####################################
# File contains all of the OOP for the start screen, which is first displayed
# when __main__ is run. It also contains all of the OOP for the scoreboard,
# which is used to update the global high score list

#startscreen.py Citation Comment:
#Lines 12-46: Original code
#Lines 47-53: Code inspired by answer to Stack Overflow Question: How to pickle a list? [closed]
#Lines 54-62: Original code
####################################

from tkinter import *
import pickle

class Startscreen(object):
    
    def __init__(self):
        self.p1x0 = 100
        self.p1x1 = 500
        self.p1y0 = 370
        self.p1y1 = 440
        
        self.p2x0 = 100
        self.p2x1 = 500
        self.p2y0 = 480
        self.p2y1 = 550
        
        self.scorex0 = 10
        self.scorex1 = 105
        self.scorey0 = 570
        self.scorey1 = 590
        
        self.image = PhotoImage(file = "sprites/startscreen.gif")
    
    def draw(self, canvas):
        canvas.create_image(300, 300, image = self.image)
        canvas.create_rectangle(self.scorex0, self.scorey0, self.scorex1, \
            self.scorey1, fill = "orange")
        canvas.create_text(self.scorex0, self.scorey0, text = "High Scores", \
            font = "Helvetica 12 bold", anchor = "nw")

class Scoreboard(object):
    
    def __init__(self):
        self.highscores = []
    
    def getScores(self):
        with open("scoreboard.pkl", "rb") as file:
            self.highscores = pickle.load(file)
    
    def storeScores(self):
        with open("scoreboard.pkl", "wb") as file:
            pickle.dump(self.highscores, file)
    
    def checkScore(self, score):
        for entry in self.highscores:
            if score >= entry[1]:
                print("New Highscore! Enter your name:")
                name = input()
                self.highscores.insert(self.highscores.index(entry), (name, score))
                self.highscores.pop()
                break