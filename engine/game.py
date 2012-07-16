#!/usr/bin/env python

from __future__ import division, print_function

import math

import map
import gamestate
import function
import constants

# the main engine class
class Game:
    def __init__(self):
        self.maxplayers = 8
        self.servername = ""
        self.isserver = False

        #DEBUGTOOL
        self.toggle_masks = False

        self.old_states = []

        # map data
        self.map = map.Map(self, "twodforttwo_remix")

        # game states
        self.current_state = gamestate.Gamestate()
        self.previous_state = self.current_state.copy()

        # This is a hack to allow game objects to append stuff to the networking event queue without having to pass networker around
        self.sendbuffer = []

        # this accumulator is used to update the engine in fixed timesteps
        self.accumulator = 0.0
        #These variables are useful for modifying to change the offsets of objects ingame
        #DEBUGTOOL
        self.horizontal = 0
        self.vertical = 0
    def update(self, networker, frametime):
        self.accumulator += frametime

        while self.accumulator >= constants.PHYSICS_TIMESTEP:
            self.accumulator -= constants.PHYSICS_TIMESTEP

            self.previous_state = self.current_state.copy()
            self.current_state.update_all_objects(self, constants.PHYSICS_TIMESTEP)
            networker.sendbuffer += self.sendbuffer
            self.sendbuffer = []

            if not self.isserver:
                self.old_states.append(self.current_state.copy())
                self.old_states[-1].time = round(self.old_states[-1].time, 5)
                print("Old states just got enlarged:", [s.time for s in self.old_states])
