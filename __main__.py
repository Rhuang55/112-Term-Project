####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *
from buggy import *
from track import *
from obstacle import *

def init(data):
    data.buggy = Buggy()
    data.track = Track()
    data.crashed = False
    data.potholes = [Pothole().generate() for i in range(2)]

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):

    if event.keysym == "Up":
        data.buggy.keymove(0, -1)
    
    if event.keysym == "Down":
        data.buggy.keymove(0, 1)
    
    if event.keysym == "Left":
        data.buggy.keymove(-1, 0)
        
    if event.keysym == "Right":
        data.buggy.keymove(1, 0)
    
    if event.keysym == "r":
        data.crashed = False

def timerFired(data):
    if not data.crashed:
        data.crashed = data.buggy.isCollision(data.track)
        data.buggy.roll()
        data.buggy.reset()

def redrawAll(canvas, data):
    data.buggy.draw(canvas)

####################################
# Run function general framework taken from 15-112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='light green', width=0)
                                
        #added this code to run function
        data.track.draw(canvas)
        for pothole in data.potholes:
            Pothole.draw(canvas, pothole[0], pothole[1], pothole[2])
            
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 5 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(600, 400)