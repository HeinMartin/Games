import os
import numpy as np
from time import sleep, time

import keyboard

from ship import Ship
from map import Map
from utils import *

# TODO:
# - implement velocity system? -> moving position is dependant on velocity * timeStep
#  -> get time of pressed key, the longer it is pressed, the higher velocity (linearly?)
#  -> until some max v (like 3 fields at a time?)
# - implement left border for ship floating (like 2 chars away)
# - collision and consequence (explosion)

## later:
# - health -> not dead by small asteroids -> delete asteroid and make hitting animation (blinking)
# - projectile to shoot the asteroids
# - randomly generating asteroid field


class Game:
    def __init__(self, fps):
        self.fps = fps

        self.running = True

    def run(self):
        # return 0 or 1 for running game or game over
        pass

    def update(self):
        pass

    def quit(self):
        self.running = False
        keyboard.press_and_release("esc")

    def game_over(self):
        print("--- GAME OVER ---")
        self.quit()


def keyboard_bla():
    # clearConsole()
    # if keyboard.is_pressed("space"):
    # ship.animate_jump()
    
    # elif keyboard.is_pressed("q"):
    #     break
    
    # else:
        # ship.animate_idle()
    #     pass
    
    sleep(1/FPS)

if __name__=='__main__':
    # TODO: actually: FPS should not be predefined (except a max of e.g. 60)
    # it should be a information to know for animation speed
    FPS = 4 #1 / 0.1
    time_between_frames = 1/FPS

    game = Game(FPS)
    # clearConsole()

    WAIT_MAP_ROLL_SECONDS = 1

    ship = Ship()

    mapSize = (7, 79)
    map = Map(mapSize)
    map.create_map_from_string("Game/map_create.txt")

    map.insert_ship(ship)

    direction = [0, 0]
    # TODO: move to ship
    # key_moves = {
    #     "nach-links" : (0, -1),
    #     "nach-rechts" : (0, 1),
    #     "nach-unten" : (1, 0),
    #     "nach-oben" : (-1, 0)
    # }

    key_moves = {
        "a" : (0, -1),
        "d" : (0, 1),
        "s" : (1, 0),
        "w" : (-1, 0)
    }
    
    keyboard.add_hotkey("q", lambda: game.quit())

    # keyboard.add_hotkey("w", lambda: map.move_player_by(ship, (-1,0)))
    # keyboard.add_hotkey("a", lambda: map.move_player_by(ship, (0,-1)))
    # keyboard.add_hotkey("s", lambda: map.move_player_by(ship, (1, 0)))
    # keyboard.add_hotkey("d", lambda: map.move_player_by(ship, (0,1)))
        
    keyboard.add_hotkey("nach-oben", lambda: map.move_player_by(ship, (-1,0)))
    keyboard.add_hotkey("nach-links", lambda: map.move_player_by(ship, (0,-1)))
    keyboard.add_hotkey("nach-unten", lambda: map.move_player_by(ship, (1, 0)))
    keyboard.add_hotkey("nach-rechts", lambda: map.move_player_by(ship, (0,1)))
    
    start_frame = time()
    fps = 0
    MAX_FPS = 60
    # start_time = time()
    # frame_time = 0

    rolling_timer = time()
    # main loop
    while game.running:
        # TODO: lock to 60 FPS max (not yet needed)
        if (time() - start_frame) < (1/MAX_FPS):
            continue
        
        clearConsole()
        if (time() - rolling_timer) > WAIT_MAP_ROLL_SECONDS:
            # print("roll")
            map.roll_map(ship)
            rolling_timer = time()
        
        fps = 1 / (time() - start_frame)
        print(f"{fps:.0f} FPS")
        start_frame = time()

        map.draw_map(outline=True)

        state = map.move_player_by(ship, direction)
        if state == -1:
            game.game_over()

        # sleep(1/FPS)

