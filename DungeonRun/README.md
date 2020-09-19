# MF.JAM's Dungeon Run
Project contains all the source code of the solution of the assignment `Dungeon Run`.

# Dependencies [![PyPI pyversions](https://img.shields.io/badge/python-3.7-blue)]()
Imported modules from pythons are:
- import OS
- import random
- import time
- import sys

### Usage
    python dungeon.py
    
### To Play
1. Download dungeon.py
2. You probably put dungeon.py  file in your Downloads folder.
3. Open the python console and load the game, you can do this by:
4. In Linux or Mac OS open a terminal and type python -i dungeon.py
5. In Windows, open Power Shell and type \Python3.7\python.exe -i dungeon.py
6. The game is ready to play. To see some simple instructions, type print(HELP)

### User Input Instructions
- 1 : Start with the username input
- 2 : The player chooses a type of hero
- 3 : The player may enter a name for his character (the name may not already be saved)
- 4 : Each created character automatically saved to load another time
- 5 : The player chooses the size of the adventure; small, decent orlarge
- 6 : The player is allowed to choose in which cornerof the map they want to start
- 7 : The player decides which way they want to go to get a new room. W for go up, S for down, A for left and D for right
- 8 : Following can be happen when a player inter into the room:
        a. Fight with monsters (if there are any in the room)
        b. Collect taxes (if any, and if the player is still alive)
        c. Choose which direction the player should continue to walk
- 9 :  If the player enters an already visited room, they can only choose to move on
- 10 : The adventure ends when the player leaves the map or is defeated
- 11 : When an adventure ends, the collected treasures are added to the saved game character.You can thus play several adventures with the same saved character to collect treasures
- 12 : QUIT

### ToDo
- Due to the time constraints we can not work on GUI.
- But there is always space to modify and add GUI on this program.

All the actions of these buttons shows output in the console

### Author
   *MF.JAM*
