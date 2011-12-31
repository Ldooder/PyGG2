from __future__ import division, print_function

import math, pygame
from pygame.locals import *

import function

# this file contains all kinds of constants

GAME_WIDTH = 800
GAME_HEIGHT = 600

PHYSICS_TIMESTEP = 1/60 # always update physics in these steps

# networking
INPUT_SEND_FPS = 1/30 # we send input to the server at this rate
MAX_PACKET_SIZE = 2048

# Networked Events
EVENT_HELLO = 0
EVENT_PLAYER_JOIN = 1
EVENT_PLAYER_LEAVE = 2
FULL_UPDATE = 3
SNAPSHOT_UPDATE = 4
INPUTSTATE = 5
EVENT_LEFTMOUSEBUTTON_DOWN = 6
EVENT_RIGHTMOUSEBUTTON_DOWN = 7
EVENT_PLAYER_CHANGETEAM = 8
EVENT_PLAYER_CHANGECLASS = 9
EVENT_JUMP = 10

# Class Constants - To use only in networking
CLASS_SCOUT = 0
CLASS_PYRO = 1
CLASS_SOLDIER = 2
CLASS_HEAVY = 3
CLASS_DEMOMAN = 4
CLASS_MEDIC = 5
CLASS_ENGINEER = 6
CLASS_SPY = 7
CLASS_SNIPER = 8
CLASS_QUOTE = 9
