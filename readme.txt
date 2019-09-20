############################################################################################
If you are reading this, it means you've found your way to Ryan Huang's 15112 Term Project!
This readme will contains the following sections:
1. About the project
2. Gameplay
3. Controls
4. How to run the game
############################################################################################


1. About the Project
############################################################################################
The Term Project is an infamous three-week-long final assignment in Carnegie Mellon 
University's 15112 course. For the project, I decided to create a game that runs on tkinter
called Buggy Bash. This game is inspired by the sport of buggy, which is a longstanding 
tradition at CMU (google "CMU buggy" to learn more!), where the user controls a buggy that
drives along an infinitely generated track. While doing so, the user must avoid crashing the
buggy into the curb, and must avoid hitting pedestrians or potholes. At the same time, the
user is incentivized to drive through flags which spawn next to the curb. If they can
successfully do so, they will receive one of three power-ups! This game has a single player
mode, as well as a local multiplayer. In single player mode, the user controls a buggy
designed after Apex Buggy's newest buggy (built in 2019), Solaris! In two player mode, the
first player controls Solaris, while the second player controls SDC's buggy Avarice.

2. Gameplay
#############################################################################################
In Section 1. I gave a brief overview of how the game works. In this section, I will talk
about specific interactions and nuances for each game mode!

The user is first presented with a start screen. They can use their cursor to select the
desired game mode. The user then spawns on the track with three lives. A major objective of
the game is to avoid obstacles, and crashing into them will cause the user to lose a life.
Ways to lose lives include crashing into the curb, crashing into a pothole, hitting a
pedestrian, or driving fully off of the screen. If the user crashes into a pothole or hits a
pedestrian, the obstacle will be removed from the game. Additionally, losing a life will
grant the user immunity for two seconds, during which they cannot lose lives, and can remove
obstacles from the game without penalization! Immunity is indicated by the buggy blinking.

However, there are ways to improve your chances of survival! By driving through a flag, the
user is randomly granted one of three power-ups: a pothole remover, a pedestrian remover, or
an extra life. Pothole and pedestrian removers are indicated by icons on the corner of the
screen, and using one will remove all potholes or pedestrians from the track, respectively.
A user can only have one of these removers each, but no worries, if the user has one, no more
will be granted to them! Gaining an extra life will provide the user with another life.

The objective in single player mode is to try and get as high of a score as possible. Score is
displayed at the top-left of the screen, and will automatically increase by one every second.
Additionally, driving through a flag increases your score by five! The game also has a global
high score list for single player, and clicking the high score button on the start screen will
print the list out in the shell that the game is being run in (see Section 4 for details on how
to run the game). The high score list keeps track of the top five scores. If you successfully
beat one of these scores, at the end of the game, you will be asked to input your name in the
shell that the game is being run in before the "game over" screen is displayed. The high score
list will then update to include that score!

In two player mode, score is no longer kept track, and the objective is now to outsurvive your
opponent! In two player mode, both buggies are placed on the same track, and interact with the
same objects. This means that they must compete to drive through flags and collect power-ups,
as only one user can get the power-up, and if one user uses a pothole remover, the potholes
are cleared for both users. So plan your moves wisely! In both modes, once a user runs out of
lives, the game is over, and the cursor can be used to choose to play again. This will take you
back to the start screen.

3. Controls
#############################################################################################
Single player mode uses the following controls:

Up - accelerates the buggy, or makes it drive faster
Left - causes the buggy to move more leftwards as it rolls
Right - causes the buggy to move more rightwards as it rolls
Down - causes the buggy to decelerate, and if pressed enough, brake
Letter O - Uses the pothole remover
P - Uses the pedestrian remover

Note that turning right and left doesn't cause the buggy to jump to the right or left of the
screen -- they will still roll forward, but will also drive more to the left.

For two player mode, Player One, in control of Solaris, retains all of the existing controls.
Player Two is now given the following controls:

W - accelerates the buggy
A - causes the buggy to move more leftwards
S - causes the buggy to decelerate or break
D - causes the buggy to move more rightwards
C - Uses the pothole remover
V - Uses the pedestrian remover

One comment about tkinter, the module in which the animation is run: Tkinter interacts with
key pressing in the same way that your operating system will. For me, running on Windows, that
means that holding down one key causes the computer to register one key press, followed by a
short pause, and then followed by a spam of key presses. Additionally, Windows only recognizes
one key press at a time, meaning that if two keys are pressed and held down at relatively the
same time, the second of the two presses will be registered and recorded. Especially for two
player mode, it can be very difficult to control a buggy if both users are trying to hold down
keys. So, at least for operating systems like Windows which record key presses in this way, it 
is recommended to tap keys rapidly instead of holding them down to get the game to respond
the quickest!

4. How to Run the Game
############################################################################################
The entirety of the code for this project is written in Python, so you will need to download
some sort of shell to run it. I am currently running the game on Python v3.7.3. I'd imagine
that versions near this one should run it just fine, but if you are having troubles running
the game, you may want to consider running it on this version. Additionally, the game utilizes
the libraries for tkinter, math, pickle, and random. All three of these libraries were 
preinstalled for me, and I don't think you should have to install them separately, at least 
if you're running my version of Python.

To run the game, simply open the __main__.py file in your shell or editer and run it. You
should not have to open or move any other files or folders, and unless you really know what
you're doing, I'd encourage you to not do so! All of the files are location-sensitive so
moving them to other directories than they are currently in will break the game. Additionally,
if you want to open up the files and look at the code, you can (and make sure to cite
whatever you copy!), but you do not have to write any lines of code to make the game work.

############################################################################################
Thanks for reading and enjoy the game!!
############################################################################################