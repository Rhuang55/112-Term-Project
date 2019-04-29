####################################
# Name: Ryan Huang
# Andrew: rdhuang
# Section: E
####################################

from tkinter import *
from math import *
from buggy import *
from track import *
from obstacle import *
from powerup import *

def init(data):
    data.buggy = Buggy()
    data.track = Track()
    data.crashed = False
    data.drawBuggy = True
    data.immuneTime = 0
    data.potholes = []
    data.pedestrians = []
    data.yellowLines = [[295, 305, 305, 295, -60]] + \
        [data.track.makeYellowLines(i) for i in range(data.height) \
        if i % 120 == 60]
    data.timeClock = 0

def keyPressed(event, data):

    if event.keysym == "Up":
        data.buggy.accelerate()
    
    if event.keysym == "Down":
        data.buggy.brake()
    
    if event.keysym == "Left":
        data.buggy.turnLeft()
        
    if event.keysym == "Right":
        data.buggy.turnRight()

def timerFired(data):
    if not data.crashed:
        data.buggy.roll()
        newLines = []
        newPedestrians = []
        newPotholes = []
        
        if data.track.isCollision(data.buggy) and data.buggy.immune == False:
            crash(data)
        
        for pothole in data.potholes:
            pothole.y += 1
            pothole.moveX()
            if pothole.isCollision(data.buggy) and data.buggy.immune == False:
                crash(data)
                newPotholes.append(pothole)
            elif pothole.y > 600 + pothole.r:
                pass
            else:
                newPotholes.append(pothole)
        data.potholes = newPotholes

        for pedest in data.pedestrians:
            pedest.y += 1
            pedest.x += pedest.speed
            if pedest.isCollision(data.buggy):
                if data.buggy.immune == False:
                    crash(data)
            elif pedest.x < 0 or pedest.x > 600:
                pass
            else:
                newPedestrians.append(pedest)
        data.pedestrians = newPedestrians
        
        for line in data.yellowLines:
            if line[4] == 660:
                newLines.append([295, 305, 305, 295,-60])
            if line[4] < 660:
                newLines.append(line)
            line[4] += 1
        data.yellowLines = newLines
        
        if data.timeClock % 150 == 0:
            data.potholes.append(Pothole())
        data.timeClock += 1
        if data.timeClock % 250 == 0:
            data.pedestrians.append(Pedestrian())
        if data.buggy.immune == True:
            if data.timeClock < data.immuneTime + 200:
                timeDiff = data.timeClock - data.immuneTime
                if 0 < timeDiff <= 25 or 50 < timeDiff <= 75 \
                    or 100 < timeDiff <= 125 or 150 < timeDiff <= 175:
                        data.drawBuggy = False
                else:
                    data.drawBuggy = True
            else:
                data.buggy.immune = False
                data.drawBuggy = True

def crash(data):
    if data.buggy.lives > 1:
        data.buggy.lives -= 1
        data.buggy.immune = True
        data.immuneTime = data.timeClock
    else:
        data.crashed = True

def redrawAll(canvas, data):
    data.track.draw(canvas)
    for line in data.yellowLines:
        data.track.drawYellowLines(canvas, line)
    for pothole in data.potholes:
        pothole.draw(canvas)
    for pedest in data.pedestrians:
        pedest.draw(canvas)
    if data.drawBuggy:
        data.buggy.draw(canvas)

####################################
# Run function general framework taken from 15-112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='light green', width=0)
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
    data.timerDelay = 10 # milliseconds
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

run(600, 600)