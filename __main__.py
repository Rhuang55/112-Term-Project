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
from startscreen import *

def init(data):
    data.buggy = Buggy()
    data.track = Track()
    data.indics = Indicators()
    data.crashed = False
    data.drawBuggy = True
    data.immuneTime = 0
    data.potholes = []
    data.pedestrians = []
    data.flags = []
    data.pedestRemover = False
    data.potholeRemover = False
    data.yellowLines = [[295, 305, 305, 295, -60]] + \
        [data.track.makeYellowLines(i) for i in range(data.height) \
        if i % 120 == 60]
    data.timeClock = 0
    data.startscreen = Startscreen()
    data.start = True

def keyPressed(event, data):

    if event.keysym == "Up":
        data.buggy.accelerate()
    
    if event.keysym == "Down":
        data.buggy.brake()
    
    if event.keysym == "Left":
        data.buggy.turnLeft()
        
    if event.keysym == "Right":
        data.buggy.turnRight()
    
    if event.keysym == "o":
        if data.potholeRemover == True:
            data.potholes = []
            data.potholeRemover = False
    
    if event.keysym == "p":
        if data.pedestRemover == True:
            data.pedestrians = []
            data.pedestRemover = False

def mousePressed(event, data):
    if data.start == True:
        if data.startscreen.p1x0 <= event.x <= data.startscreen.p1x1 and \
            data.startscreen.p1y0 <= event.y <= data.startscreen.p1y1:
                data.start = False

def timerFired(data):
   
    if not data.crashed:
        newLines = []
        for line in data.yellowLines:
            if line[4] == 660:
                newLines.append([295, 305, 305, 295,-60])
            if line[4] < 660:
                newLines.append(line)
            line[4] += 1
        data.yellowLines = newLines
    
    if data.start:
        data.timeClock = 0

    if not (data.crashed or data.start):
        data.buggy.roll()
        newPedestrians = []
        newPotholes = []
        newFlags = []
        
        if data.track.isCollision(data.buggy) and data.buggy.immune == False:
            crash(data)
        
        for pothole in data.potholes:
            pothole.y += 1
            pothole.moveX()
            if pothole.isCollision(data.buggy) and data.buggy.immune == False:
                crash(data)
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
        
        for flag in data.flags:
            flag.y += 1
            flag.moveX()
            if flag.isCollision(data.buggy):
                getPowerUp(data)
            elif flag.y - flag.height > 600:
                pass
            else:
                newFlags.append(flag)
            data.flags = newFlags
        
        if data.timeClock % 150 == 0: #every 1.5 seconds
            data.potholes.append(Pothole())
        data.timeClock += 1
        if data.timeClock % 250 == 0:
            data.pedestrians.append(Pedestrian())
        if data.timeClock % 500 == 0:
            data.flags.append(Flag())
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
        data.buggy.lives -= 1
        data.crashed = True

def getPowerUp(data):
    options = ["lives"]
    if data.pedestRemover == False:
        options.append("pedest")
    if data.potholeRemover == False:
        options.append("pothole")

    powerUp = choice(options)
    if powerUp == "pothole":
        data.potholeRemover = True
    if powerUp == "pedest":
        data.pedestRemover = True
    if powerUp == "lives":
        data.buggy.lives += 1

def redrawAll(canvas, data):
    if not data.start == True:
        data.track.draw(canvas)
        for line in data.yellowLines:
            data.track.drawYellowLines(canvas, line)
        for flag in data.flags:
            flag.draw(canvas)
        for pothole in data.potholes:
            pothole.draw(canvas)
        for pedest in data.pedestrians:
            pedest.draw(canvas)
        if data.drawBuggy:
            data.buggy.draw(canvas)
        drawLifeIndic(canvas, data)
        drawPowerUpIndic(canvas, data)
    else:
        data.track.draw(canvas)
        for line in data.yellowLines:
            data.track.drawYellowLines(canvas, line)
        data.startscreen.draw(canvas)

def drawLifeIndic(canvas, data):
    data.indics.drawHeart(canvas)
    canvas.create_text(25, 25, text = data.buggy.lives, \
        font = "Helvetica 12 bold", fill = "white")

def drawPowerUpIndic(canvas, data):
    canvas.create_rectangle(535, 0, 600, 30, fill = "white", width = 0)
    canvas.create_line(535, 0, 535, 30, width = 2)
    canvas.create_line(600, 30, 535, 30, width = 2)
    canvas.create_line(567, 0, 567, 30, width = 2)
    if data.potholeRemover == True:
        data.indics.drawPothole(canvas)
    if data.pedestRemover == True:
        data.indics.drawPedest(canvas)

####################################
# Run function general framework taken from 15-112 course notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
####################################

def run(width=600, height=600):
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