from utils import *

import time


class Ship:
    def __init__(self):

        self.velocity = 0


        self.idle_static = ">" #"$"
        self.idle_animation = ["$"] # ["\n._$", "\n_.$"] # idle must be inside the game loop, otherwise it will block keyboard input while animation runs!!!
        self.jump_animation = ["$"] # ["\n._$", "  $\n./", "._$\n", "\n\'\\$", "\n._$"]
        """"
        ._$
        
        $
        /    "  $\n /\n\'"
        '

        $
        ./

        ._$

        
        '\$

        ._$

        """

    def display_to_pitch(self, toDisplay):
        print(toDisplay)

    def animate_idle(self):
        for idle in self.idle_animation:
            clearConsole()
            self.display_to_pitch(idle)
            time.sleep(1/FPS)

    def animate_jump(self):
        for jump in self.jump_animation:
            clearConsole()
            self.display_to_pitch(jump)
            time.sleep(1/FPS)


### testing things
def testChars():
    cont = ["a", "b", "c", "!", "\"", "-", "_", "<", "|"]
    n = 10

    for ch in cont:
        print(n*".")
        print(n*ch)

    print(n*".")
    print(n//2 *"_ ")